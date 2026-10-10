import os
import json

def verify_clusters():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, "Correlation", "correlated_clusters.json")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        clusters = json.load(f)
        
    print(f"Total Clusters: {len(clusters)}")
    print("-" * 50)
    
    # Let's find an interesting cluster (e.g. contains multiple nodes and different log families)
    interesting_cluster = None
    for c in clusters:
        nodes_involved = set(e['node_id'] for e in c['events'])
        families_involved = set(e['log_family'] for e in c['events'])
        
        # We want a juicy incident: cross-node, with faults and triggers
        if len(nodes_involved) > 1 and 'Fault History' in families_involved and 'Operator Interaction' in families_involved:
            interesting_cluster = c
            break
            
    if not interesting_cluster:
        print("Could not find a cross-node cluster with both Operator Interactions and Faults.")
        # Fallback to the largest cluster
        interesting_cluster = max(clusters, key=lambda x: x['event_count'])
        
    print(f"--- VERIFICATION OF CLUSTER: {interesting_cluster['cluster_id']} ---")
    print(f"Duration: {interesting_cluster['start_time']} to {interesting_cluster['end_time']}")
    print(f"Total Unique Events: {interesting_cluster['event_count']}")
    
    nodes = set(e['node_id'] for e in interesting_cluster['events'])
    print(f"Nodes Involved: {', '.join(nodes)}")
    
    print("\nTIMELINE:")
    for event in interesting_cluster['events']:
        time = event['timestamp'].split('T')[1]
        node = event['node_id']
        family = event['log_family']
        summary = event['event_summary']
        occ = event.get('occurrences', 1)
        occ_str = f"(x{occ} times)" if occ > 1 else ""
        print(f"[{time}] {node} | {family.ljust(20)} | {summary} {occ_str}")
        
if __name__ == "__main__":
    verify_clusters()
