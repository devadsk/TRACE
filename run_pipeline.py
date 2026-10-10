"""
TRACE - Timeline Reconstruction and Correlation Engine
Master Pipeline Runner

Orchestrates all 5 stages of the TRACE forensic analysis pipeline:

  Stage 1 | Ingestion          -- Parses NODE_A/B/C HTML logs -> normalized_events.jsonl
  Stage 2 | Correlation        -- Clusters events into causal incident groups
  Stage 3 | Timeline           -- Compiles each cluster into a Markdown transcript
  Stage 4 | AI Forensic Report -- Generates full forensic narrative per incident
  Stage 5 | Visualization      -- Bundles all data into viz_data.js / viz_data.json

Usage:
  python run_pipeline.py                          # Full pipeline (deterministic AI)
  python run_pipeline.py --skip-ingest            # Skip Stage 1, reuse existing data
  python run_pipeline.py --use-llm                # Stage 4 uses Gemini LLM (needs .env)
  python run_pipeline.py --serve                  # Run pipeline then launch dashboard
  python run_pipeline.py --serve-only             # Just launch dashboard (no pipeline)
  python run_pipeline.py --stages 1,2,3           # Run only specific stages
  python run_pipeline.py --port 9090              # Custom dashboard port
  python run_pipeline.py --no-browser             # Do not auto-open browser

Author: TRACE Development Team -- Honeywell Aerospace
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import subprocess
import time
import webbrowser
import http.server
import socketserver
import threading
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# COLOUR TERMINAL OUTPUT HELPERS
# ---------------------------------------------------------------------------

BOLD  = "\033[1m"
RED   = "\033[91m"
GREEN = "\033[92m"
AMBER = "\033[93m"
BLUE  = "\033[94m"
CYAN  = "\033[96m"
RESET = "\033[0m"
DIM   = "\033[2m"


def hdr(text: str) -> None:
    print(f"\n{BOLD}{BLUE}{'=' * 70}{RESET}")
    print(f"{BOLD}{BLUE}  {text}{RESET}")
    print(f"{BOLD}{BLUE}{'=' * 70}{RESET}")


def ok(text: str) -> None:
    print(f"  {GREEN}[OK]{RESET}  {text}")


def warn(text: str) -> None:
    print(f"  {AMBER}[!!]{RESET}  {text}")


def err(text: str) -> None:
    print(f"  {RED}[XX]{RESET}  {text}")


def info(text: str) -> None:
    print(f"  {CYAN}[ >]{RESET}  {text}")


# ---------------------------------------------------------------------------
# PATH CONSTANTS
# ---------------------------------------------------------------------------

ROOT = Path(__file__).parent.resolve()

PATHS = {
    "node_dir":            ROOT / "NODE",
    "ingestion_main":      ROOT / "Ingestion" / "main.py",
    "normalized_events":   ROOT / "Ingestion" / "normalized_events.jsonl",
    "correlator":          ROOT / "Correlation" / "correlator.py",
    "correlated_clusters": ROOT / "Correlation" / "correlated_clusters.json",
    "compiler":            ROOT / "Timeline" / "compiler.py",
    "transcripts_dir":     ROOT / "Timeline" / "transcripts",
    "ai_reporter_dir":     ROOT / "AI_Reporter",
    "narrator":            ROOT / "AI_Reporter" / "standalone_narrator.py",
    "reporter":            ROOT / "AI_Reporter" / "reporter.py",
    "final_reports_dir":   ROOT / "AI_Reporter" / "final_reports",
    "viz_dir":             ROOT / "Visualization",
    "viz_data_json":       ROOT / "Visualization" / "viz_data.json",
    "viz_data_js":         ROOT / "Visualization" / "viz_data.js",
}

_DEFAULT_PORT = 8080


# ---------------------------------------------------------------------------
# STAGE 1 -- LOG INGESTION
# ---------------------------------------------------------------------------

def stage_1_ingestion(skip: bool = False) -> bool:
    """Calls Ingestion/main.py -> main(). Parses NODE HTML logs."""
    ne = PATHS["normalized_events"]
    if skip and ne.exists():
        ok(f"Skipping ingestion -- reusing {ne.stat().st_size/1e6:.1f} MB normalized_events.jsonl")
        return True
    if skip:
        warn("--skip-ingest: file not found, running ingestion anyway")

    info("Calling Ingestion/main.py -> main() ...")
    sys.path.insert(0, str(ROOT / "Ingestion"))
    try:
        import main as ingestion_main  # type: ignore
        import importlib; importlib.reload(ingestion_main)  # safe reload for re-runs
        ingestion_main.main()
    except Exception as exc:
        err(f"Ingestion error: {exc}"); return False

    if not ne.exists():
        err("normalized_events.jsonl was not created."); return False

    event_count = sum(1 for _ in ne.open(encoding="utf-8"))
    ok(f"Ingestion complete -- {event_count:,} events ({ne.stat().st_size/1e6:.1f} MB)")
    return True


# ---------------------------------------------------------------------------
# STAGE 2 -- CORRELATION ENGINE
# ---------------------------------------------------------------------------

def stage_2_correlation() -> bool:
    """Calls Correlation/correlator.py -> run_correlation()."""
    if not PATHS["normalized_events"].exists():
        err("normalized_events.jsonl not found -- run Stage 1 first.")
        return False

    info("Calling Correlation/correlator.py -> run_correlation() ...")
    sys.path.insert(0, str(ROOT / "Correlation"))
    try:
        import correlator  # type: ignore
        import importlib; importlib.reload(correlator)
        correlator.run_correlation()
    except Exception as exc:
        err(f"Correlation error: {exc}"); return False

    cc = PATHS["correlated_clusters"]
    if not cc.exists():
        err("correlated_clusters.json was not created."); return False

    with open(cc, encoding="utf-8") as f:
        clusters = json.load(f)
    ok(f"Correlation complete -- {len(clusters):,} incident clusters")
    return True


# ---------------------------------------------------------------------------
# STAGE 3 -- TIMELINE COMPILATION
# ---------------------------------------------------------------------------

def stage_3_timeline() -> bool:
    """Calls Timeline/compiler.py -> main(). Compiles Markdown transcripts."""
    if not PATHS["correlated_clusters"].exists():
        err("correlated_clusters.json not found -- run Stage 2 first.")
        return False

    info("Calling Timeline/compiler.py -> main() ...")
    sys.path.insert(0, str(ROOT / "Timeline"))
    try:
        import compiler as timeline_compiler  # type: ignore
        import importlib; importlib.reload(timeline_compiler)
        timeline_compiler.main()
    except Exception as exc:
        err(f"Timeline error: {exc}"); return False

    transcripts = list(PATHS["transcripts_dir"].glob("*.md"))
    ok(f"Timeline complete -- {len(transcripts):,} Markdown transcripts written")
    return True


# ---------------------------------------------------------------------------
# STAGE 4 -- FORENSIC NARRATION (DETERMINISTIC OR LLM)
# ---------------------------------------------------------------------------

def stage_4_forensic_reports(use_llm: bool = False) -> bool:
    """Generate full forensic narrative reports per incident cluster."""
    td = PATHS["transcripts_dir"]
    if not td.exists() or not list(td.glob("*.md")):
        err("No transcripts found -- run Stage 3 first.")
        return False

    PATHS["final_reports_dir"].mkdir(parents=True, exist_ok=True)

    if use_llm:
        env_file = PATHS["ai_reporter_dir"] / ".env"
        if not env_file.exists():
            warn(".env not found in AI_Reporter/ -- falling back to deterministic narrator")
            use_llm = False
        else:
            info("Using Gemini LLM for forensic reports (reporter.py) ...")
            result = subprocess.run(
                [sys.executable, str(PATHS["reporter"])],
                cwd=str(PATHS["ai_reporter_dir"]),
            )
            if result.returncode != 0:
                warn(f"LLM reporter exited with code {result.returncode} -- some reports may use fallback")

    if not use_llm:
        info("Using deterministic ForensicNarrator for reports ...")
        _run_standalone_narrator()

    reports = list(PATHS["final_reports_dir"].glob("REPORT_*.md"))
    ok(f"Forensic narration complete -- {len(reports):,} reports generated")
    return True


def _run_standalone_narrator() -> None:
    """Directly invoke ForensicNarrator on all transcript files."""
    sys.path.insert(0, str(PATHS["ai_reporter_dir"]))
    try:
        from standalone_narrator import ForensicNarrator  # type: ignore
    except ImportError as exc:
        err(f"Cannot import ForensicNarrator: {exc}")
        return

    narrator = ForensicNarrator()
    transcripts = sorted(PATHS["transcripts_dir"].glob("*.md"))
    total = len(transcripts)

    for idx, tp in enumerate(transcripts, 1):
        rp = PATHS["final_reports_dir"] / f"REPORT_{tp.name}"

        # Skip already-verified reports
        if rp.exists():
            content = rp.read_text(encoding="utf-8")
            if len(content.strip()) > 500 and "## 6." in content:
                if idx % 20 == 0 or idx == total:
                    info(f"Skipped {idx}/{total} (already verified)")
                continue

        md = tp.read_text(encoding="utf-8")
        try:
            report = narrator.narrate_transcript(md, cluster_id=tp.stem)
            rp.write_text(report, encoding="utf-8")
        except Exception as exc:
            warn(f"Narrator error on {tp.name}: {exc}")

        if idx % 25 == 0 or idx == total:
            print(f"  {DIM}Progress: {idx}/{total} ({idx/total*100:.0f}%){RESET}", flush=True)


# ---------------------------------------------------------------------------
# STAGE 5 -- VISUALIZATION DATASET PACKAGING
# ---------------------------------------------------------------------------

_SEV_KEYWORDS = {
    "CRITICAL": ["critical", "total loss", "dual mode", "single mode", "failover",
                 "crash", "abort", "emergency", "fire", "smoke"],
    "HIGH":     ["high", "degraded", "fault", "failure", "error", "warning", "alert"],
    "WARNING":  ["warning", "warn", "caution", "minor", "intermittent"],
}


def _infer_severity(text: str, cluster: dict) -> str:
    low = text.lower()
    for sev, kws in _SEV_KEYWORDS.items():
        if any(kw in low for kw in kws):
            return sev
    families = set(ev.get("log_family", "") for ev in cluster.get("events", []))
    if "Fault History" in families:
        return "WARNING"
    if "State Transition" in families:
        return "HIGH"
    return "INFORMATIONAL"


def _between(text: str, start_h: str, others: list) -> str:
    lines = text.splitlines()
    capturing = False
    buf = []
    for line in lines:
        ll = line.lower().strip()
        if not capturing:
            if start_h.lower() in ll and ll.startswith("##"):
                capturing = True
            continue
        if ll.startswith("##") and any(h.lower() in ll for h in others):
            break
        buf.append(line)
    return "\n".join(buf).strip()


def _parse_report(md: str, cluster: dict):
    all_h = ["executive summary", "root cause", "failure cascade",
             "system impact", "corrective", "incident overview", "recommended"]
    exec_s  = _between(md, "executive summary", all_h)
    root_c  = _between(md, "root cause", all_h)
    cascade = _between(md, "failure cascade", all_h)
    impact  = _between(md, "system impact", all_h)
    correct = _between(md, "corrective", all_h)

    sev = "INFORMATIONAL"
    for line in md.splitlines():
        ll = line.lower()
        for s in ("critical", "high", "warning", "informational"):
            if s in ll and ("|" in ll or "severity" in ll or "rating" in ll):
                sev = s.upper()
                break

    if sev == "INFORMATIONAL":
        sev = _infer_severity(md + exec_s + root_c, cluster)

    if not exec_s:
        first = "\n".join(l for l in md.splitlines() if l.strip() and not l.startswith("#"))
        exec_s = first[:400].strip()

    return exec_s, root_c, cascade, impact, correct, sev


def _derive_from_cluster(cluster: dict):
    events = cluster.get("events", [])
    families = sorted(set(ev.get("log_family", "") for ev in events))
    nodes    = sorted(set(ev.get("node_id", "") for ev in events))
    summaries = list(set(ev.get("event_summary", "") for ev in events[:5]))
    has_fault = any("Fault" in f for f in families)
    has_state = any("State" in f for f in families)
    sev = "WARNING" if has_fault else ("HIGH" if has_state else "INFORMATIONAL")
    summary = (
        f"Incident on {', '.join(nodes)} involving {', '.join(families)}. "
        f"Key events: {'; '.join(summaries[:3])}."
    )
    return sev, summary


def stage_5_package_visualization() -> bool:
    """Bundle clusters + forensic reports into viz_data.json and viz_data.js."""
    cf = PATHS["correlated_clusters"]
    if not cf.exists():
        err("correlated_clusters.json not found -- run Stage 2 first.")
        return False

    info("Loading correlated clusters ...")
    with open(cf, encoding="utf-8") as f:
        clusters = json.load(f)
    info(f"Loaded {len(clusters)} clusters.")

    rd = PATHS["final_reports_dir"]
    info("Merging forensic reports into visualization dataset ...")

    incidents = []
    for idx, cluster in enumerate(clusters, 1):
        cid = cluster["cluster_id"]
        rp  = rd / f"REPORT_{cid}.md"

        full_md = ""
        exec_s  = ""
        root_c  = ""
        cascade = ""
        impact  = ""
        correct = ""
        sev     = "INFORMATIONAL"

        if rp.exists():
            full_md = rp.read_text(encoding="utf-8")
            exec_s, root_c, cascade, impact, correct, sev = _parse_report(full_md, cluster)
        else:
            sev, exec_s = _derive_from_cluster(cluster)
            root_c = exec_s
            full_md = f"# {cid}\n\n{exec_s}"

        events_out = []
        for ev in cluster.get("events", []):
            ts = ev.get("timestamp", "")
            events_out.append({
                "event_id":      ev.get("event_id", ""),
                "timestamp":     ts,
                "time_str":      ts.split("T")[-1][:8] if "T" in ts else ts[:8],
                "node_id":       ev.get("node_id", ""),
                "log_family":    ev.get("log_family", ""),
                "event_summary": ev.get("event_summary", ""),
                "occurrences":   ev.get("occurrences", 1),
                "source_file":   ev.get("source_file", ""),
                "sequence_id":   ev.get("sequence_id", ""),
                "raw_payload":   ev.get("raw_payload", {}),
            })

        start_ts = cluster.get("start_time", "")
        end_ts   = cluster.get("end_time", "")
        start_clock = start_ts.split("T")[-1][:8] if "T" in start_ts else start_ts[:8]
        end_clock   = end_ts.split("T")[-1][:8]   if "T" in end_ts   else end_ts[:8]

        try:
            duration_sec = max(0, int((
                datetime.fromisoformat(end_ts) - datetime.fromisoformat(start_ts)
            ).total_seconds()))
        except Exception:
            duration_sec = 0

        nodes = sorted(set(ev.get("node_id", "") for ev in cluster.get("events", [])))

        incidents.append({
            "index":              idx,
            "cluster_id":         cid,
            "start_time":         start_ts,
            "end_time":           end_ts,
            "start_clock":        start_clock,
            "end_clock":          end_clock,
            "duration_sec":       duration_sec,
            "nodes":              nodes,
            "event_count":        cluster.get("event_count", len(events_out)),
            "raw_occurrences":    cluster.get("total_occurrences_incl_duplicates",
                                              cluster.get("event_count", len(events_out))),
            "severity":           sev,
            "executive_summary":  exec_s,
            "root_cause":         root_c,
            "cascade_sequence":   cascade,
            "system_impact":      impact,
            "corrective_actions": correct,
            "full_markdown":      full_md,
            "events":             events_out,
        })

        if idx % 25 == 0 or idx == len(clusters):
            print(f"  {DIM}Packaged {idx}/{len(clusters)} incidents{RESET}", flush=True)

    # Write viz_data.json
    info("Writing viz_data.json ...")
    with open(PATHS["viz_data_json"], "w", encoding="utf-8") as f:
        json.dump(incidents, f, indent=2, ensure_ascii=False)
    ok(f"viz_data.json written ({PATHS['viz_data_json'].stat().st_size / 1024:.0f} KB)")

    # Write viz_data.js
    info("Writing viz_data.js ...")
    with open(PATHS["viz_data_js"], "w", encoding="utf-8") as f:
        f.write("window.TRACE_INCIDENTS = ")
        json.dump(incidents, f, indent=2, ensure_ascii=False)
        f.write(";\n")
    ok(f"viz_data.js written ({PATHS['viz_data_js'].stat().st_size / 1024:.0f} KB, "
       f"{len(incidents)} incidents)")
    return True


# ---------------------------------------------------------------------------
# DASHBOARD SERVER
# ---------------------------------------------------------------------------

def launch_dashboard(port: int = _DEFAULT_PORT, open_browser: bool = True) -> None:
    """Serve Visualization/ via HTTP and open the browser."""
    viz_dir = PATHS["viz_dir"]
    if not viz_dir.exists():
        err(f"Visualization directory not found: {viz_dir}")
        return

    os.chdir(viz_dir)

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
        def log_error(self, *a):   pass

    def _serve(p: int) -> bool:
        try:
            with socketserver.TCPServer(("", p), QuietHandler) as httpd:
                url = f"http://127.0.0.1:{p}/index.html"
                print(f"\n  {GREEN}[OK]{RESET}  Dashboard live -> {BOLD}{url}{RESET}")
                print(f"  {DIM}Press Ctrl+C to stop the server{RESET}\n")
                if open_browser:
                    threading.Timer(0.8, webbrowser.open, args=(url,)).start()
                httpd.serve_forever()
        except OSError:
            return False
        return True

    if not _serve(port):
        warn(f"Port {port} busy, trying {port + 1} ...")
        if not _serve(port + 1):
            err("Could not bind to any port. Is the dashboard already running?")


# ---------------------------------------------------------------------------
# ARGUMENT PARSING
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        prog="run_pipeline.py",
        description="TRACE -- Timeline Reconstruction and Correlation Engine\n"
                    "Master pipeline runner for the full forensic analysis workflow.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--skip-ingest",  action="store_true",
                   help="Skip Stage 1 and reuse existing normalized_events.jsonl")
    p.add_argument("--use-llm",      action="store_true",
                   help="Stage 4: use Gemini LLM (requires AI_Reporter/.env)")
    p.add_argument("--serve",        action="store_true",
                   help="Launch dashboard after pipeline completes")
    p.add_argument("--serve-only",   action="store_true",
                   help="Skip pipeline, only launch dashboard")
    p.add_argument("--port",         type=int, default=_DEFAULT_PORT,
                   help=f"HTTP port for dashboard (default: {_DEFAULT_PORT})")
    p.add_argument("--stages",       type=str, default="1,2,3,4,5",
                   help="Comma-separated stage list (default: 1,2,3,4,5)")
    p.add_argument("--no-browser",   action="store_true",
                   help="Do not auto-open browser when serving")
    return p.parse_args()


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main() -> int:
    args = parse_args()

    print(f"""
{BOLD}{BLUE}+======================================================================+
|  TRACE -- Timeline Reconstruction and Correlation Engine             |
|  Honeywell Aerospace Avionics Forensic Analysis Pipeline             |
+======================================================================+{RESET}
""")
    wall_start = time.monotonic()

    if args.serve_only:
        hdr("Dashboard Server")
        launch_dashboard(port=args.port, open_browser=not args.no_browser)
        return 0

    try:
        run_stages = set(int(s.strip()) for s in args.stages.split(","))
    except ValueError:
        err(f"Invalid --stages value: {args.stages!r}. Example: --stages 1,2,3")
        return 1

    results: dict = {}

    # Stage 1
    if 1 in run_stages:
        hdr("Stage 1 -- Ingestion")
        t0 = time.monotonic()
        flag = stage_1_ingestion(skip=args.skip_ingest)
        results[1] = flag
        (ok if flag else err)(f"Stage 1 in {time.monotonic()-t0:.1f}s")
        if not flag:
            err("Halting pipeline.")
            return 1
    else:
        info("Stage 1 (Ingestion) -- SKIPPED")

    # Stage 2
    if 2 in run_stages:
        hdr("Stage 2 -- Correlation Engine")
        t0 = time.monotonic()
        flag = stage_2_correlation()
        results[2] = flag
        (ok if flag else err)(f"Stage 2 in {time.monotonic()-t0:.1f}s")
        if not flag:
            err("Halting pipeline.")
            return 1
    else:
        info("Stage 2 (Correlation) -- SKIPPED")

    # Stage 3
    if 3 in run_stages:
        hdr("Stage 3 -- Timeline Compilation")
        t0 = time.monotonic()
        flag = stage_3_timeline()
        results[3] = flag
        (ok if flag else err)(f"Stage 3 in {time.monotonic()-t0:.1f}s")
        if not flag:
            err("Halting pipeline.")
            return 1
    else:
        info("Stage 3 (Timeline) -- SKIPPED")

    # Stage 4
    if 4 in run_stages:
        mode = "Gemini LLM" if args.use_llm else "Deterministic Narrator"
        hdr(f"Stage 4 -- Forensic Narration ({mode})")
        t0 = time.monotonic()
        flag = stage_4_forensic_reports(use_llm=args.use_llm)
        results[4] = flag
        (ok if flag else warn)(f"Stage 4 in {time.monotonic()-t0:.1f}s")
    else:
        info("Stage 4 (Forensic Narration) -- SKIPPED")

    # Stage 5
    if 5 in run_stages:
        hdr("Stage 5 -- Visualization Dataset Packaging")
        t0 = time.monotonic()
        flag = stage_5_package_visualization()
        results[5] = flag
        (ok if flag else err)(f"Stage 5 in {time.monotonic()-t0:.1f}s")
        if not flag:
            err("Halting pipeline -- visualization data could not be built.")
            return 1
    else:
        info("Stage 5 (Visualization) -- SKIPPED")

    # Summary
    total = time.monotonic() - wall_start
    hdr("Pipeline Complete")
    print(f"  Total time : {BOLD}{total:.1f}s{RESET}")
    print(f"  Stages run : {', '.join(str(s) for s in sorted(run_stages))}")
    for s, r in sorted(results.items()):
        status = f"{GREEN}PASS{RESET}" if r else f"{RED}FAIL{RESET}"
        print(f"  Stage {s}    : [{status}]")

    # Launch dashboard if requested
    if args.serve:
        hdr("Dashboard Server")
        launch_dashboard(port=args.port, open_browser=not args.no_browser)

    return 0


if __name__ == "__main__":
    sys.exit(main())

