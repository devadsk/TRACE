"""
Stage 5 (Narrate) + Verifier

Generates rich, evidence-linked incident narratives citing real record IDs (#ID),
incorporating multi-node corroboration consensus, cross-node clock drift,
and Level 3 operational context (flight phase and guidance mode).

The closed-loop verifier guarantees 0 ungrounded citations and 0 missing evidence IDs.
"""

import re
from typing import Set, Tuple

def narrate_incident(inc, events_by_id) -> str:
    all_ids = inc.fault_event_ids + inc.recovery_event_ids
    cite = " ".join(f"#{i}" for i in all_ids)
    
    nodes = sorted(inc.nodes_reporting_fault)
    if len(nodes) == 1:
        node_str = f"node {nodes[0]}"
    elif len(nodes) == 2:
        node_str = f"nodes {' and '.join(nodes)}"
    else:
        node_str = f"all three nodes ({', '.join(nodes)})"

    # Operational context phrasing
    ctx_parts = []
    if inc.context and inc.context.phase != "UNKNOWN":
        ctx_parts.append(f"During {inc.context.phase} phase")
    if inc.context and inc.context.guidance_mode != "UNKNOWN":
        ctx_parts.append(f"under {inc.context.guidance_mode} guidance")
    
    intro = ", ".join(ctx_parts)
    if intro:
        intro += f", flight {inc.flight} experienced"
    else:
        intro = f"On flight {inc.flight},"

    base = (
        f"{intro} fault {inc.fault_code} (\"{inc.eicas}\", {inc.severity}) "
        f"at {inc.onset_ts}, reported by {node_str}."
    )

    # Clock drift & consensus detail
    if inc.clock_drift_ms > 0:
        base += f" Cross-node detection skew was measured at {inc.clock_drift_ms:.1f}ms."

    if inc.duplicate_count > 0:
        base += f" {inc.duplicate_count} bus chatter duplicate alert line(s) were recorded."

    # Pilot interaction context
    if inc.context and inc.context.prior_pilot_action and inc.context.prior_action_delta_s is not None:
        base += f" Preceding MCDU interaction '{inc.context.prior_pilot_action}' occurred {inc.context.prior_action_delta_s:.1f}s prior to alert onset."

    # Recovery status
    if inc.resolved:
        base += (
            f" Recovery was confirmed {inc.recovery_duration_s:.1f}s later, "
            f"corroborated across {len(inc.nodes_reporting_recovery)} node(s)."
        )
    else:
        base += " No matching recovery record was found within the 120s window — flagged as UNRESOLVED (critical evidence gap)."

    base += f" Corroboration confidence: {inc.confidence_label}. Auditable evidence: {cite}."
    return base

def verify_narrative(text: str, valid_ids: Set[str]) -> Tuple[bool, Set[str], Set[str]]:
    """
    Validates that:
    1. Every cited ID in the text exists in the incident's valid evidence set.
    2. Every required evidence ID in valid_ids is cited at least once.
    """
    cited = set(re.findall(r"#(\w+)", text))
    bad = cited - valid_ids
    missing = valid_ids - cited
    is_valid = (len(bad) == 0) and (len(missing) == 0)
    return is_valid, bad, missing
