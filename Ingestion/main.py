import os
import json
import logging
from parsers import (
    AircraftStateParser,
    FaultHistoryParser,
    OperatorInteractionParser,
    SoftwareEventParser,
    StateTransitionParser
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_node_id(filename: str) -> str:
    if filename.startswith("NODE_A"):
        return "NODE_A"
    elif filename.startswith("NODE_B"):
        return "NODE_B"
    elif filename.startswith("NODE_C"):
        return "NODE_C"
    return "UNKNOWN_NODE"

def get_parser(filename: str):
    if "Aircraft_State" in filename:
        return AircraftStateParser()
    elif "FAULT_REPOSITORY" in filename:
        return FaultHistoryParser()
    elif "FM_CI_BPQ" in filename:
        return OperatorInteractionParser()
    elif "FM_LBPQ" in filename:
        return SoftwareEventParser()
    elif "State_Transition" in filename:
        return StateTransitionParser()
    return None

def main():
    node_dir = r"d:\TRACE\NODE"
    output_dir = r"d:\TRACE\Ingestion"
    output_file = os.path.join(output_dir, "normalized_events.jsonl")
    skipped_file = os.path.join(output_dir, "skipped_records.jsonl")
    
    os.makedirs(output_dir, exist_ok=True)
    # Ensure fresh output files
    for f in [output_file, skipped_file]:
        if os.path.exists(f):
            os.remove(f)

    if not os.path.exists(node_dir):
        logging.error(f"Directory not found: {node_dir}")
        return

    all_events = []

    for filename in os.listdir(node_dir):
        if not filename.endswith(".html"):
            continue
            
        filepath = os.path.join(node_dir, filename)
        node_id = get_node_id(filename)
        parser = get_parser(filename)
        
        if not parser:
            logging.warning(f"No parser found for file: {filename}")
            continue
            
        logging.info(f"Processing {filename} with {parser.__class__.__name__}...")
        events = parser.parse_file(filepath, node_id, skipped_file)
        all_events.extend(events)
        logging.info(f"Extracted {len(events)} events from {filename}.")
        
    # Sort all events chronologically
    logging.info("Sorting all events chronologically by timestamp...")
    # Filtering out events with unparseable timestamps just in case, but keeping them at the top
    all_events.sort(key=lambda x: x.timestamp)
    
    # Write to output file
    logging.info(f"Writing {len(all_events)} normalized events to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        for event in all_events:
            f.write(event.to_json() + '\n')
            
    logging.info("Phase 1 Complete!")

if __name__ == "__main__":
    main()
