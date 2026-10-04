"""
Stage 1 (Ingest) + Stage 2 (Normalize)

One adapter per log family / file format. Each adapter is independent —
if one format changes, only its adapter needs editing. Every successfully
parsed record becomes a common Event; anything unparseable is counted and
reported, never silently dropped.
"""

import csv
import json
import re
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Event:
    id: str
    node: str
    flight: str
    family: str
    t: float            # seconds since epoch-ish, for sorting/windowing
    ts: str              # original timestamp string
    code: str            # primary event code/type
    detail: dict = field(default_factory=dict)

def parse_ts(ts: str) -> float:
    """Fast ISO timestamp parser with microsecond and Z support."""
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.timestamp()
    except Exception:
        # Fallback for unexpected formats
        try:
            dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S")
        return dt.timestamp()

def parse_kv_string(raw: str) -> dict:
    """Parses key=value comma- or space-separated telemetry strings into a dictionary."""
    data = {}
    if not raw:
        return data
    for token in raw.replace(",", " ").split():
        if "=" in token:
            k, v = token.split("=", 1)
            data[k.strip()] = v.strip()
        else:
            data.setdefault("extra", []).append(token.strip())
    return data

class Ingestor:
    def __init__(self):
        self.events = []
        self.skipped = []   # (family, raw_line, reason)
        self._next_id = 1

    def _new_id(self):
        rid = f"R{self._next_id:06d}"
        self._next_id += 1
        return rid

    # ---------- Adapter 1: operator_interaction.csv ----------
    def ingest_operator_csv(self, path):
        family = "operator_interaction"
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                raw = ",".join(row)
                try:
                    if len(row) != 5:
                        raise ValueError(f"expected 5 fields, got {len(row)}")
                    ts, flight, node, action, detail = row
                    parsed_detail = parse_kv_string(detail)
                    parsed_detail["raw"] = detail
                    self.events.append(Event(
                        id=self._new_id(), node=node, flight=flight, family=family,
                        t=parse_ts(ts), ts=ts, code=action, detail=parsed_detail
                    ))
                except Exception as e:
                    self.skipped.append((family, raw, str(e)))

    # ---------- Adapter 2: guidance_planning.jsonl ----------
    def ingest_guidance_jsonl(self, path):
        family = "guidance_planning"
        with open(path, encoding="utf-8") as f:
            for line in f:
                raw = line.strip()
                if not raw:
                    self.skipped.append((family, raw, "blank line"))
                    continue
                try:
                    obj = json.loads(raw)
                    self.events.append(Event(
                        id=self._new_id(), node=obj["node"], flight=obj["flight"], family=family,
                        t=parse_ts(obj["ts"]), ts=obj["ts"], code=obj["event"],
                        detail={"mode": obj.get("mode")}
                    ))
                except Exception as e:
                    self.skipped.append((family, raw, str(e)))

    # ---------- Adapter 3: state_transition.log (key=value) ----------
    def ingest_state_log(self, path):
        family = "state_transition"
        pattern = re.compile(
            r"ts=(?P<ts>\S+) flight=(?P<flight>\S+) node=(?P<node>\S+) "
            r"phase=(?P<phase>\S+) prev=(?P<prev>\S+)"
        )
        with open(path, encoding="utf-8") as f:
            for line in f:
                raw = line.strip()
                if not raw:
                    self.skipped.append((family, raw, "blank line"))
                    continue
                m = pattern.match(raw)
                if not m:
                    self.skipped.append((family, raw, "regex mismatch"))
                    continue
                d = m.groupdict()
                try:
                    self.events.append(Event(
                        id=self._new_id(), node=d["node"], flight=d["flight"], family=family,
                        t=parse_ts(d["ts"]), ts=d["ts"], code=f"PHASE_{d['phase']}",
                        detail={"phase": d["phase"], "prev": d["prev"]}
                    ))
                except Exception as e:
                    self.skipped.append((family, raw, str(e)))

    # ---------- Adapter 4: fault_event.txt (EICAS-bracketed) ----------
    def ingest_fault_txt(self, path):
        family = "fault_event"
        pattern = re.compile(
            r'\[(?P<ts>[^\]]+)\] (?P<flight>\S+) (?P<node>\S+) '
            r'EICAS="(?P<eicas>[^"]+)" CODE=(?P<code>\S+) ATA=(?P<ata>\S+) SEV=(?P<sev>\S+)'
        )
        with open(path, encoding="utf-8") as f:
            for line in f:
                raw = line.strip()
                if not raw:
                    self.skipped.append((family, raw, "blank line"))
                    continue
                m = pattern.match(raw)
                if not m:
                    self.skipped.append((family, raw, "regex mismatch"))
                    continue
                d = m.groupdict()
                try:
                    self.events.append(Event(
                        id=self._new_id(), node=d["node"], flight=d["flight"], family=family,
                        t=parse_ts(d["ts"]), ts=d["ts"], code="FAULT",
                        detail={"fault_code": d["code"], "eicas": d["eicas"],
                                "ata": d["ata"], "severity": d["sev"]}
                    ))
                except Exception as e:
                    self.skipped.append((family, raw, str(e)))

    # ---------- Adapter 5: recovery_event.dat (pipe-delimited) ----------
    def ingest_recovery_dat(self, path):
        family = "recovery_event"
        with open(path, encoding="utf-8") as f:
            for line in f:
                raw = line.strip()
                if not raw:
                    self.skipped.append((family, raw, "blank line"))
                    continue
                parts = raw.split("|")
                try:
                    if len(parts) != 6:
                        raise ValueError(f"expected 6 fields, got {len(parts)}")
                    ts, flight, node, code, status, dur_ms = parts
                    self.events.append(Event(
                        id=self._new_id(), node=node, flight=flight, family=family,
                        t=parse_ts(ts), ts=ts, code="RECOVERY",
                        detail={"fault_code": code, "status": status, "duration_ms": int(dur_ms)}
                    ))
                except Exception as e:
                    self.skipped.append((family, raw, str(e)))

    def run_all(self, base_dir="dataset"):
        self.ingest_operator_csv(f"{base_dir}/operator_interaction.csv")
        self.ingest_guidance_jsonl(f"{base_dir}/guidance_planning.jsonl")
        self.ingest_state_log(f"{base_dir}/state_transition.log")
        self.ingest_fault_txt(f"{base_dir}/fault_event.txt")
        self.ingest_recovery_dat(f"{base_dir}/recovery_event.dat")
        self.events.sort(key=lambda e: e.t)
        return self.events, self.skipped
