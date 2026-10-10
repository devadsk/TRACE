import json
import os

def filter_payload(payload: dict) -> str:
    """Removes empty, redundant, or useless fields from the raw payload to save tokens."""
    noise_values = {'-', 'Not applicable', 'Invalid', '0', '0.000000', '', ' '}
    redundant_keys = {'Sequence number', 'Date and time', 'Raw Application Data'}
    
    clean_details = []
    for key, value in payload.items():
        if key in redundant_keys:
            continue
        # Handle nested dicts (like 'Message')
        if isinstance(value, dict):
            nested_clean = []
            for k, v in value.items():
                if str(v).strip() not in noise_values:
                    nested_clean.append(f"{k}: {v}")
            if nested_clean:
                clean_details.append(f"[{' | '.join(nested_clean)}]")
        else:
            if str(value).strip() not in noise_values:
                clean_details.append(f"{key}: {value}")
                
    return " | ".join(clean_details)

def compile_cluster_to_markdown(cluster: dict, output_dir: str):
    cluster_id = cluster['cluster_id']
    start_time = cluster['start_time'].split('T')[1]
    end_time = cluster['end_time'].split('T')[1]
    date = cluster['start_time'].split('T')[0]
    
    nodes = sorted(list(set(e['node_id'] for e in cluster['events'])))
    
    md_content = [
        f"# Incident Cluster: {cluster_id}",
        f"**Date:** {date}",
        f"**Duration:** {start_time} to {end_time}",
        f"**Nodes Involved:** {', '.join(nodes)}",
        f"**Total Events:** {cluster['event_count']} (Filtered from {cluster['total_occurrences_incl_duplicates']} raw logs)",
        "\n## Timeline Transcript\n"
    ]
    
    # Group by second
    timeline = {}
    for event in cluster['events']:
        time_sec = event['timestamp'].split('T')[1]
        if time_sec not in timeline:
            timeline[time_sec] = []
        timeline[time_sec].append(event)
        
    for time_sec in sorted(timeline.keys()):
        md_content.append(f"**[{time_sec}]**")
        for event in timeline[time_sec]:
            node = event['node_id']
            family = event['log_family']
            summary = event['event_summary']
            occ = event.get('occurrences', 1)
            
            occ_str = f" (x{occ} occurrences collapsed)" if occ > 1 else ""
            
            details = filter_payload(event.get('raw_payload', {}))
            
            # Format Citations. 
            source = event.get('source_file', 'Unknown_Source')
            seq = event.get('sequence_id', 'N/A')
            uuid = event.get('event_id', 'N/A')
            
            md_content.append(f"* **{node}** [{family}]{occ_str}: {summary}")
            if details:
                md_content.append(f"  * *Details:* {details}")
            md_content.append(f"  * *Citation:* `[Source: {source} | Seq: {seq} | UUID: {uuid}]`")
            
        md_content.append("") # Blank line between seconds
        
    filepath = os.path.join(output_dir, f"{cluster_id}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(md_content))

def main():
    input_file = r"d:\TRACE\Correlation\correlated_clusters.json"
    output_dir = r"d:\TRACE\Timeline\transcripts"
    
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return
        
    with open(input_file, 'r', encoding='utf-8') as f:
        clusters = json.load(f)
        
    print(f"Compiling {len(clusters)} clusters into Markdown transcripts...")
    
    for cluster in clusters:
        compile_cluster_to_markdown(cluster, output_dir)
        
    print(f"Success! {len(clusters)} Markdown files written to {output_dir}")

if __name__ == "__main__":
    # Ensure base directory exists
    os.makedirs(r"d:\TRACE\Timeline", exist_ok=True)
    main()
