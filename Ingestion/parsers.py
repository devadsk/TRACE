import os
import json
import uuid
import logging
import traceback
from bs4 import BeautifulSoup
from dateutil import parser as date_parser
from models import NormalizedEvent

class BaseParser:
    log_family = "Unknown"

    def parse_file(self, filepath, node_id, skipped_records_file):
        events = []
        skipped = []
        filename = os.path.basename(filepath)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
        except Exception as e:
            logging.error(f"Failed to open/parse {filepath}: {e}")
            return [], []

        table = soup.find('table', class_='log-table')
        if not table:
            return [], []

        rows = table.find_all('tr')
        if not rows:
            return [], []

        headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]

        for i, row in enumerate(rows[1:], start=2):
            try:
                cells = row.find_all(['td', 'th'])
                if len(cells) != len(headers):
                    raise ValueError(f"Column count mismatch: expected {len(headers)}, got {len(cells)}")
                
                row_data = {}
                for j in range(len(headers)):
                    header = headers[j]
                    cell = cells[j]
                    
                    msg_div = cell.find('div', class_='msg')
                    if msg_div and msg_div.find('ul'):
                        li_items = msg_div.find('ul').find_all('li')
                        sub_dict = {}
                        for li in li_items:
                            strong = li.find('strong')
                            if strong:
                                key = strong.get_text(strip=True).rstrip(':')
                                value = li.get_text(strip=True)[len(strong.get_text()):].strip()
                                sub_dict[key] = value
                        row_data[header] = sub_dict
                    else:
                        row_data[header] = cell.get_text(strip=True)
                
                event_id = str(uuid.uuid4())
                event = self._parse_row(row_data, node_id, filename, event_id)
                if event:
                    events.append(event)
            except Exception as e:
                skipped.append({
                    "file": filepath,
                    "line_approx": i,
                    "error": str(e),
                    "traceback": traceback.format_exc(),
                    "raw_html": str(row)
                })

        if skipped:
            with open(skipped_records_file, 'a', encoding='utf-8') as sf:
                for s in skipped:
                    sf.write(json.dumps(s) + '\n')

        return events

    def _parse_row(self, row_data, node_id, source_file, event_id) -> NormalizedEvent:
        raise NotImplementedError

class FaultHistoryParser(BaseParser):
    log_family = "Fault History"

    def _parse_row(self, row_data, node_id, source_file, event_id) -> NormalizedEvent:
        seq_id = row_data.get("Serial Number", row_data.get("Sequence number", ""))
        date_str = row_data.get("Date and Time", row_data.get("Date and time", ""))
        timestamp = date_parser.parse(date_str).isoformat() if date_str else ""

        fault_name = row_data.get("Fault Name", "")
        fault_code = row_data.get("Fault Code", "")
        summary = f"{fault_name} (Code: {fault_code})" if fault_code else fault_name
        if not summary:
            summary = "Fault Event"

        return NormalizedEvent(
            event_id=event_id,
            timestamp=timestamp,
            node_id=node_id,
            log_family=self.log_family,
            source_file=source_file,
            sequence_id=str(seq_id),
            event_summary=summary,
            raw_payload=row_data
        )

class AircraftStateParser(BaseParser):
    log_family = "Aircraft State"
    
    def _parse_row(self, row_data, node_id, source_file, event_id) -> NormalizedEvent:
        seq_id = row_data.get("Sequence number", "")
        date_str = row_data.get("Date and time", "")
        timestamp = date_parser.parse(date_str).isoformat() if date_str else ""
        
        return NormalizedEvent(
            event_id=event_id,
            timestamp=timestamp,
            node_id=node_id,
            log_family=self.log_family,
            source_file=source_file,
            sequence_id=str(seq_id),
            event_summary="Aircraft State Update",
            raw_payload=row_data
        )

class OperatorInteractionParser(BaseParser):
    log_family = "Operator Interaction"
    
    def _parse_row(self, row_data, node_id, source_file, event_id) -> NormalizedEvent:
        seq_id = row_data.get("Sequence number", "")
        date_str = row_data.get("Date and time", "")
        timestamp = date_parser.parse(date_str).isoformat() if date_str else ""
        
        summary = "Operator Interaction Event"
        msg = row_data.get("Message", {})
        if isinstance(msg, dict):
            summary = msg.get("Operator Interaction Event", summary)
            
        return NormalizedEvent(
            event_id=event_id,
            timestamp=timestamp,
            node_id=node_id,
            log_family=self.log_family,
            source_file=source_file,
            sequence_id=str(seq_id),
            event_summary=summary,
            raw_payload=row_data
        )

class SoftwareEventParser(BaseParser):
    log_family = "Software Event"
    
    def _parse_row(self, row_data, node_id, source_file, event_id) -> NormalizedEvent:
        seq_id = row_data.get("Sequence number", "")
        date_str = row_data.get("Date and time", "")
        timestamp = date_parser.parse(date_str).isoformat() if date_str else ""
        
        summary = "Software Event"
        data_id = row_data.get("Data Identifier")
        if data_id:
            summary = f"Software Event: {data_id}"
            
        return NormalizedEvent(
            event_id=event_id,
            timestamp=timestamp,
            node_id=node_id,
            log_family=self.log_family,
            source_file=source_file,
            sequence_id=str(seq_id),
            event_summary=summary,
            raw_payload=row_data
        )

class StateTransitionParser(BaseParser):
    log_family = "State Transition"
    
    def _parse_row(self, row_data, node_id, source_file, event_id) -> NormalizedEvent:
        seq_id = row_data.get("Sequence number", "")
        date_str = row_data.get("Date and time", "")
        timestamp = date_parser.parse(date_str).isoformat() if date_str else ""
        
        summary = "State Transition"
        msg = row_data.get("Message", {})
        if isinstance(msg, dict):
            master_status = msg.get("Master status")
            if master_status:
                summary = f"State Transition: Master status -> {master_status}"
                
        return NormalizedEvent(
            event_id=event_id,
            timestamp=timestamp,
            node_id=node_id,
            log_family=self.log_family,
            source_file=source_file,
            sequence_id=str(seq_id),
            event_summary=summary,
            raw_payload=row_data
        )
