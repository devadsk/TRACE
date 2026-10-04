"""
TRACE pipeline — full run against the ~4,500-record practice dataset.
Ingest -> Normalize -> Correlate -> Graph/Corroboration -> Narrate -> Verify

Produces:
- results/summary.txt       (human-readable benchmark report)
- results/incidents.json     (rich causal incidents with Level 3 context & clock drift)
- results/events.json        (normalized events index for Level 4 raw drill-down)
- results/skipped.json       (audited unparsed records with reasons)
- results/narratives.json    (verified ground-truth narratives)
"""

import json
import os
import time
from collections import Counter
from ingest import Ingestor
from correlate import build_incidents
from narrate import narrate_incident, verify_narrative

def main():
    start_time = time.time()
    ing = Ingestor()
    events, skipped = ing.run_all(base_dir="dataset")
    events_by_id = {e.id: e for e in events}
    valid_ids = set(events_by_id.keys())

    incidents = build_incidents(events)

    lines = []
    def p(s=""):
        lines.append(s)
        print(s)

    p("=" * 70)
    p("TRACE PIPELINE: EXECUTION & BENCHMARK REPORT")
    p("=" * 70)
    p("STAGE 1-2: INGEST + NORMALIZE (5 Log Families)")
    p("-" * 70)
    fam_counts = Counter(e.family for e in events)
    for fam, cnt in fam_counts.items():
        p(f"  {fam:24} {cnt:5} events parsed")
    p(f"  {'TOTAL parsed':24} {len(events):5}")
    p(f"  {'TOTAL skipped (audited)':24} {len(skipped):5}  ({len(skipped)/(len(events)+len(skipped))*100:.2f}% of all raw lines)")

    skip_by_family = Counter(s[0] for s in skipped)
    p("\n  Skipped breakdown by family:")
    for fam, cnt in skip_by_family.items():
        p(f"    {fam:22} {cnt:4} skipped")
    p("\n  Sample skipped records (first 5):")
    for fam, raw, reason in skipped[:5]:
        p(f"    [{fam}] '{raw[:50]}'  -> {reason}")

    p("\n" + "=" * 70)
    p("STAGE 3-4: CORRELATE + GRAPH / CORROBORATION SCORING")
    p("-" * 70)
    p(f"  Total incidents reconstructed: {len(incidents)}")
    conf_dist = Counter(i.confidence_label for i in incidents)
    for label, cnt in sorted(conf_dist.items()):
        p(f"    {label:32} {cnt:4}")
    
    resolved = sum(1 for i in incidents if i.resolved)
    unresolved = len(incidents) - resolved
    p(f"\n  Resolved (recovery confirmed): {resolved}/{len(incidents)}")
    p(f"  Unresolved / evidence gap:     {unresolved}/{len(incidents)}")
    dup_total = sum(i.duplicate_count for i in incidents)
    p(f"  Duplicate alert lines absorbed: {dup_total}")
    avg_drift = sum(i.clock_drift_ms for i in incidents if i.clock_drift_ms > 0) / max(1, sum(1 for i in incidents if i.clock_drift_ms > 0))
    p(f"  Mean multi-node clock skew:    {avg_drift:.2f} ms")

    p("\n" + "=" * 70)
    p("STAGE 5: NARRATE + VERIFY (Sample of first 5 incidents)")
    p("-" * 70)
    verify_pass = 0
    verify_fail = 0
    all_narratives = []

    for inc in incidents:
        text = narrate_incident(inc, events_by_id)
        # Ensure we only check evidence IDs pertaining to this incident
        incident_evidence_ids = set(inc.fault_event_ids + inc.recovery_event_ids)
        ok, bad, missing = verify_narrative(text, incident_evidence_ids)
        if ok:
            verify_pass += 1
        else:
            verify_fail += 1
        all_narratives.append({
            "incident_id": inc.incident_id,
            "narrative": text,
            "verified": ok,
            "bad_citations": list(bad),
            "missing_citations": list(missing)
        })

    for n in all_narratives[:5]:
        p(f"\n  [{n['incident_id']}] (verified={n['verified']})")
        p(f"  {n['narrative']}")

    p("\n" + "-" * 70)
    p(f"VERIFIER RESULT: {verify_pass}/{len(incidents)} narratives passed citation check ({verify_fail} failed)")
    elapsed = round(time.time() - start_time, 3)
    p(f"Total pipeline execution time: {elapsed}s")
    p("-" * 70)

    # ---- Export structured outputs for 4-Level Visualization ----
    os.makedirs("results", exist_ok=True)
    with open("results/summary.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Export rich incidents
    with open("results/incidents.json", "w", encoding="utf-8") as f:
        json.dump([{
            "incident_id": i.incident_id,
            "flight": i.flight,
            "fault_code": i.fault_code,
            "eicas": i.eicas,
            "severity": i.severity,
            "ata": i.ata,
            "onset": i.onset_ts,
            "nodes_reporting_fault": sorted(i.nodes_reporting_fault),
            "nodes_reporting_recovery": sorted(i.nodes_reporting_recovery),
            "clock_drift_ms": i.clock_drift_ms,
            "confidence": i.confidence_label,
            "confidence_score": i.confidence_score,
            "resolved": i.resolved,
            "recovery_duration_s": i.recovery_duration_s,
            "duplicate_count": i.duplicate_count,
            "evidence_ids": i.fault_event_ids + i.recovery_event_ids,
            "fault_event_ids": i.fault_event_ids,
            "recovery_event_ids": i.recovery_event_ids,
            "context": {
                "phase": i.context.phase,
                "prev_phase": i.context.prev_phase,
                "guidance_mode": i.context.guidance_mode,
                "prior_pilot_action": i.context.prior_pilot_action,
                "prior_action_detail": i.context.prior_action_detail,
                "prior_action_delta_s": i.context.prior_action_delta_s,
                "context_event_ids": i.context.context_event_ids
            }
        } for i in incidents], f, indent=2)

    # Export raw events for Level 4 drill-down
    with open("results/events.json", "w", encoding="utf-8") as f:
        json.dump({
            e.id: {
                "id": e.id,
                "node": e.node,
                "flight": e.flight,
                "family": e.family,
                "t": e.t,
                "ts": e.ts,
                "code": e.code,
                "detail": e.detail
            } for e in events
        }, f, indent=2)

    # Export skipped audit
    with open("results/skipped.json", "w", encoding="utf-8") as f:
        json.dump([{
            "family": s[0],
            "raw": s[1],
            "reason": s[2]
        } for s in skipped], f, indent=2)

    with open("results/narratives.json", "w", encoding="utf-8") as f:
        json.dump(all_narratives, f, indent=2)

    # Export JS bundle for zero-server direct browser execution
    with open("results/data_bundle.js", "w", encoding="utf-8") as f:
        f.write("window.TRACE_BUNDLE = {\n")
        f.write(f"  summary: {json.dumps(lines)},\n")
        with open("results/incidents.json", "r", encoding="utf-8") as inc_f:
            f.write(f"  incidents: {inc_f.read()},\n")
        with open("results/events.json", "r", encoding="utf-8") as ev_f:
            f.write(f"  events: {ev_f.read()},\n")
        with open("results/skipped.json", "r", encoding="utf-8") as sk_f:
            f.write(f"  skipped: {sk_f.read()},\n")
        with open("results/narratives.json", "r", encoding="utf-8") as nar_f:
            f.write(f"  narratives: {nar_f.read()}\n")
        f.write("};\n")

    print("\nWrote results/summary.txt, results/incidents.json, results/events.json, results/skipped.json, results/narratives.json, results/data_bundle.js")

if __name__ == "__main__":
    main()
