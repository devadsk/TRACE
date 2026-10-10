import json
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, Any

@dataclass
class NormalizedEvent:
    event_id: str
    timestamp: str  # using ISO string for easier JSON serialization
    node_id: str
    log_family: str
    source_file: str
    sequence_id: str
    event_summary: str
    raw_payload: Dict[str, Any]

    def to_json(self) -> str:
        return json.dumps(asdict(self))
