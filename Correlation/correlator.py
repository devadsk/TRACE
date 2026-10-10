import json
import os
import uuid
from datetime import datetime
from typing import List, Dict

class Correlator:
    def __init__(self, time_window_sec=60, score_threshold=15):
        self.time_window_sec = time_window_sec
        self.score_threshold = score_threshold
        
    def deduplicate(self, raw_events: List[Dict]) -> List[Dict]:
        if not raw_events:
            return []
            
        deduped = []
        current_event = raw_events[0].copy()
        current_event['occurrences'] = 1
        current_event['raw_event_ids'] = [current_event.get('event_id', '')]
        
        for next_event in raw_events[1:]:
            # If same timestamp, node, family, and summary -> Collapse them
            if (current_event['timestamp'] == next_event['timestamp'] and
                current_event['node_id'] == next_event['node_id'] and
                current_event['log_family'] == next_event['log_family'] and
                current_event['event_summary'] == next_event['event_summary']):
                
                current_event['occurrences'] += 1
                current_event['raw_event_ids'].append(next_event.get('event_id', ''))
            else:
                deduped.append(current_event)
                current_event = next_event.copy()
                current_event['occurrences'] = 1
                current_event['raw_event_ids'] = [current_event.get('event_id', '')]
                
        deduped.append(current_event)
        return deduped

    def calculate_score(self, event_a: Dict, event_b: Dict) -> int:
        score = 0
        
        t_a = datetime.fromisoformat(event_a['timestamp'])
        t_b = datetime.fromisoformat(event_b['timestamp'])
        diff = abs((t_b - t_a).total_seconds())
        
        if diff > self.time_window_sec:
            return 0
            
        # Same Node
        if event_a['node_id'] == event_b['node_id']:
            score += 10
            
        # Cause/Effect relationship (Trigger -> Reaction)
        triggers = {'Operator Interaction', 'State Transition'}
        reactions = {'Fault History', 'Software Event'}
        families = {event_a['log_family'], event_b['log_family']}
        if (families & triggers) and (families & reactions):
            score += 15
            
        # Context Vectors
        p_a = event_a.get('raw_payload', {})
        p_b = event_b.get('raw_payload', {})
        
        # Flight Leg Match
        leg_a = p_a.get('Flight Leg Number') or p_a.get('Flight leg num')
        leg_b = p_b.get('Flight Leg Number') or p_b.get('Flight leg num')
        if leg_a is not None and leg_b is not None and leg_a == leg_b:
            score += 5
            
        # Flight Phase Match
        phase_a = p_a.get('Flight Phase')
        phase_b = p_b.get('Flight Phase')
        if phase_a is not None and phase_b is not None and phase_a == phase_b:
            score += 5
            
        # Cross-Node Logic: Communication or Status messages
        msg_a = str(p_a.get('Message', ''))
        msg_b = str(p_b.get('Message', ''))
        if 'Master' in msg_a and 'Master' in msg_b:
            score += 5
            
        return score

    def build_graph(self, events: List[Dict]):
        edges = []
        n = len(events)
        
        for i in range(n):
            t_i = datetime.fromisoformat(events[i]['timestamp'])
            for j in range(i + 1, n):
                t_j = datetime.fromisoformat(events[j]['timestamp'])
                # Array is chronologically sorted, so break early to save processing
                if abs((t_j - t_i).total_seconds()) > self.time_window_sec:
                    break
                
                score = self.calculate_score(events[i], events[j])
                if score >= self.score_threshold:
                    edges.append((i, j))
                    
        return edges

    def extract_clusters(self, events: List[Dict], edges: List[tuple]) -> List[Dict]:
        n = len(events)
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        clusters = []
        
        for i in range(n):
            if i not in visited:
                cluster_nodes = []
                stack = [i]
                visited.add(i)
                while stack:
                    curr = stack.pop()
                    cluster_nodes.append(curr)
                    for neighbor in adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                            
                cluster_nodes.sort()
                cluster_events = [events[idx] for idx in cluster_nodes]
                
                # Format cluster summary
                cluster = {
                    "cluster_id": f"cluster-{uuid.uuid4().hex[:8]}",
                    "start_time": cluster_events[0]['timestamp'],
                    "end_time": cluster_events[-1]['timestamp'],
                    "event_count": len(cluster_events),
                    "total_occurrences_incl_duplicates": sum(e.get('occurrences', 1) for e in cluster_events),
                    "events": cluster_events
                }
                clusters.append(cluster)
                
        # Filter out clusters that are just 1 event with 1 occurrence (noise)
        # For aviation, we generally care about cascading faults (multiple events) 
        # or major faults that didn't cascade. We will return all for completeness.
        return clusters

def run_correlation():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, "Ingestion", "normalized_events.jsonl")
    output_file = os.path.join(base_dir, "Correlation", "correlated_clusters.json")
    
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return

    print("Loading normalized events...")
    raw_events = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                raw_events.append(json.loads(line))
                
    print(f"Loaded {len(raw_events)} events.")
    
    correlator = Correlator(time_window_sec=60, score_threshold=15)
    
    print("Deduplicating events...")
    deduped_events = correlator.deduplicate(raw_events)
    print(f"Reduced dataset to {len(deduped_events)} deduplicated events.")
    
    print("Scoring event relationships (Graph Edges)...")
    edges = correlator.build_graph(deduped_events)
    print(f"Identified {len(edges)} causal/contextual links between events.")
    
    print("Extracting connected components (Clusters)...")
    clusters = correlator.extract_clusters(deduped_events, edges)
    
    # Sort clusters chronologically
    clusters.sort(key=lambda x: x['start_time'])
    
    print(f"Successfully collapsed events into {len(clusters)} distinct incident clusters.")
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(clusters, f, indent=2)
        
    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    run_correlation()
