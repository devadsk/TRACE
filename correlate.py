"""
Stage 3 (Correlate) + Stage 4 (Graph / Corroboration Scoring) + Operational Context Linking

Groups fault + recovery events into incidents per (flight, fault_code) within a time window,
scores cross-node corroboration confidence, measures exact cross-node clock drift,
and links Level 3 operational context (phase, guidance mode, pilot interaction).

Deterministic and mathematically auditable — zero hallucination.
"""

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set

CORRELATION_WINDOW_S = 5.0   # fault lines within this window = same incident
RECOVERY_WINDOW_S = 120.0    # recovery within this window matches the fault

@dataclass
class OperationalContext:
    phase: str = "UNKNOWN"
    prev_phase: Optional[str] = None
    guidance_mode: str = "UNKNOWN"
    prior_pilot_action: Optional[str] = None
    prior_action_detail: Optional[dict] = None
    prior_action_delta_s: Optional[float] = None
    context_event_ids: List[str] = field(default_factory=list)

@dataclass
class Incident:
    incident_id: str
    flight: str
    fault_code: str
    eicas: str = ""
    severity: str = "UNKNOWN"
    ata: str = ""
    onset_t: float = 0.0
    onset_ts: str = ""
    fault_event_ids: List[str] = field(default_factory=list)
    recovery_event_ids: List[str] = field(default_factory=list)
    nodes_reporting_fault: Set[str] = field(default_factory=set)
    nodes_reporting_recovery: Set[str] = field(default_factory=set)
    clock_drift_ms: float = 0.0
    duplicate_count: int = 0
    resolved: bool = False
    recovery_duration_s: Optional[float] = None
    confidence_score: int = 0
    confidence_label: str = ""
    context: OperationalContext = field(default_factory=OperationalContext)

def build_incidents(events) -> List[Incident]:
    # 1. Partition events by flight for linear, isolated processing
    events_by_flight = defaultdict(list)
    for e in events:
        events_by_flight[e.flight].append(e)

    incidents: List[Incident] = []
    inc_counter = 1
    used_recovery_ids = set()

    # Process flight by flight in stable order
    for flight in sorted(events_by_flight.keys()):
        flight_events = sorted(events_by_flight[flight], key=lambda e: e.t)
        faults = [e for e in flight_events if e.code == "FAULT"]
        recoveries = [e for e in flight_events if e.code == "RECOVERY"]
        state_events = [e for e in flight_events if e.family == "state_transition"]
        guidance_events = [e for e in flight_events if e.family == "guidance_planning"]
        operator_events = [e for e in flight_events if e.family == "operator_interaction"]

        used_fault_ids = set()

        for e in faults:
            if e.id in used_fault_ids:
                continue

            fc = e.detail.get("fault_code", "UNKNOWN")
            group = [e]
            used_fault_ids.add(e.id)

            # Two-pointer / linear window scan across subsequent faults on this flight
            for other in faults:
                if other.id in used_fault_ids:
                    continue
                if other.detail.get("fault_code") == fc and (other.t - e.t) <= CORRELATION_WINDOW_S and (other.t >= e.t):
                    group.append(other)
                    used_fault_ids.add(other.id)

            onset_t = min(g.t for g in group)
            onset_e = min(group, key=lambda g: g.t)
            nodes_fault = {g.node for g in group}
            dup_count = len(group) - len(nodes_fault)

            # Compute cross-node clock drift in milliseconds
            if len(group) > 1:
                clock_drift_ms = round((max(g.t for g in group) - min(g.t for g in group)) * 1000, 2)
            else:
                clock_drift_ms = 0.0

            # Level 3: Operational Context Extraction
            # Active flight phase at onset
            prior_states = [s for s in state_events if s.t <= onset_t]
            active_phase = prior_states[-1].detail.get("phase", "CRUISE") if prior_states else "PREFLIGHT"
            prev_phase = prior_states[-1].detail.get("prev") if prior_states else None

            # Active guidance mode at onset
            prior_guidance = [g for g in guidance_events if g.t <= onset_t]
            active_mode = prior_guidance[-1].detail.get("mode") or prior_guidance[-1].code if prior_guidance else "MANUAL"

            # Preceding pilot/operator action (within 30s)
            prior_ops = [op for op in operator_events if 0 <= (onset_t - op.t) <= 30.0]
            prior_op = prior_ops[-1] if prior_ops else None

            # Surrounding operational events (within +/- 15s) for drill-down context
            surrounding = [
                ev.id for ev in flight_events
                if abs(ev.t - onset_t) <= 15.0 and ev.family in ("state_transition", "guidance_planning", "operator_interaction")
            ]

            context = OperationalContext(
                phase=active_phase,
                prev_phase=prev_phase,
                guidance_mode=active_mode,
                prior_pilot_action=prior_op.code if prior_op else None,
                prior_action_detail=prior_op.detail if prior_op else None,
                prior_action_delta_s=round(onset_t - prior_op.t, 2) if prior_op else None,
                context_event_ids=surrounding
            )

            # Match recovery records without double-claiming
            matched_rec = [
                r for r in recoveries
                if r.id not in used_recovery_ids
                and r.detail.get("fault_code") == fc
                and 0 <= (r.t - onset_t) <= RECOVERY_WINDOW_S
            ]

            resolved = False
            rec_ids = []
            rec_nodes = set()
            recovery_dur_s = None

            if matched_rec:
                resolved = True
                rec_ids = [r.id for r in matched_rec]
                for rid in rec_ids:
                    used_recovery_ids.add(rid)
                rec_nodes = {r.node for r in matched_rec}
                recovery_dur_s = round(min(r.t for r in matched_rec) - onset_t, 3)

            score = len(nodes_fault)
            confidence_label = {
                1: "LOW (single-source)",
                2: "MEDIUM (2-node agreement)",
                3: "HIGH (full 3-node agreement)"
            }.get(score, "UNKNOWN")

            inc = Incident(
                incident_id=f"INC{inc_counter:04d}",
                flight=flight,
                fault_code=fc,
                eicas=onset_e.detail.get("eicas", fc),
                severity=onset_e.detail.get("severity", "ADVISORY"),
                ata=onset_e.detail.get("ata", fc),
                onset_t=onset_t,
                onset_ts=onset_e.ts,
                fault_event_ids=[g.id for g in group],
                recovery_event_ids=rec_ids,
                nodes_reporting_fault=nodes_fault,
                nodes_reporting_recovery=rec_nodes,
                clock_drift_ms=clock_drift_ms,
                duplicate_count=dup_count,
                resolved=resolved,
                recovery_duration_s=recovery_dur_s,
                confidence_score=score,
                confidence_label=confidence_label,
                context=context
            )
            inc_counter += 1
            incidents.append(inc)

    return incidents
