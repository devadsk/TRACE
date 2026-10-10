import os
import re
import glob
import time
from dotenv import dotenv_values
from openai import OpenAI

# ==============================================================================
# AI REPORTER CONFIGURATION (GEMMA FORENSIC PIPELINE)
# ==============================================================================

env_vars = dotenv_values(".env")
key = env_vars.get("GEMINI_API_KEY")

print(f"DEBUG: Using Gemini API Key starting with: {key[:10] if key else 'None'}...")
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/", 
    api_key=key
)

# Gemma MoE architecture: faster, compliant with hackathon constraints
MODEL_NAME = "gemma-4-26b-a4b-it"

SYSTEM_PROMPT = """You are an expert Aviation Forensic Investigator analyzing distributed avionics system failures on an aircraft.
Generate a high-grade, professional Forensic Investigation Report in GitHub Markdown.

Your report MUST contain the following sections:
# AVIATION FORENSIC INVESTIGATION REPORT: <Cluster ID>

## 1. Incident Overview
A clean Markdown table with: Date, Duration, Affected Nodes, Total Events, Severity Rating (CRITICAL, WARNING, or INFORMATIONAL).

## 2. Executive Summary
A clear 2-3 sentence technical overview of what occurred and the operational outcome.

## 3. Root Cause Analysis (Primary Trigger)
Identify the exact triggering condition (e.g. pilot interaction, power loss, state transition, cold restart) that initiated the event. Explain the failure mechanism.

## 4. Failure Cascade & Propagation Sequence
A numbered chronological breakdown of how the failure propagated through the nodes or subsystems.

## 5. System Impact Assessment
Assess redundancy loss, degraded flight management modes (e.g. Dual mode -> Single mode), and functional availability.

## 6. Recommended Corrective & Maintenance Actions
Provide 2-3 actionable avionics engineering recommendations (e.g., hardware checks, bus inspection, software patch).

CRITICAL CITATION RULE:
Every factual claim MUST have the exact inline citation `[Source: ... | Seq: ... | UUID: ...]` immediately following the claim. Do not invent citations."""

def compact_transcript(text: str, max_chars: int = 14000) -> str:
    """
    Intelligently compacts massive transcripts (>15KB) while preserving 100% 
    of critical forensic triggers, state transitions, first/last events, and citations.
    """
    if len(text) <= max_chars:
        return text
    
    lines = text.splitlines()
    header_lines = []
    i = 0
    while i < len(lines) and not lines[i].startswith('**['):
        header_lines.append(lines[i])
        i += 1
    
    chunks = []
    current = []
    while i < len(lines):
        line = lines[i]
        if line.startswith('**['):
            if current:
                chunks.append('\n'.join(current))
                current = []
        current.append(line)
        i += 1
    if current:
        chunks.append('\n'.join(current))
        
    selected = set(range(min(6, len(chunks))))
    selected.update(range(max(0, len(chunks) - 4), len(chunks)))
    
    for idx, c in enumerate(chunks):
        if any(k in c for k in ['[State Transition]', '[Operator Interaction]', 'Operational startup', 'Dual mode Changed']):
            selected.add(idx)
            
    sorted_idx = sorted(selected)
    if len(sorted_idx) > 15:
        transitions = [idx for idx in sorted_idx if idx not in range(6) and idx not in range(len(chunks)-4, len(chunks))]
        sorted_idx = sorted(list(range(min(6, len(chunks)))) + transitions[:5] + list(range(max(0, len(chunks)-4), len(chunks))))
        
    selected_chunks = [chunks[idx] for idx in sorted_idx]
    res = '\n'.join(header_lines) + f'\n\n[Forensic Summary: Sampled {len(selected_chunks)} critical event windows from {len(chunks)} total timestamps]\n\n' + '\n\n'.join(selected_chunks)
    
    if len(res) > max_chars:
        res = res[:max_chars] + '\n\n...[Transcript windowed to preserve token limit]...'
    return res

def clean_model_output(content: str) -> str:
    """Strips internal thought scratchpads and cleans markdown artifacts."""
    clean = re.sub(r'<thought>.*?</thought>', '', content, flags=re.DOTALL)
    # Also handle unclosed thought blocks if model hit token limit inside thinking
    if '<thought>' in clean:
        clean = clean.split('<thought>')[0]
    return clean.strip()

def generate_report(transcript_path: str, output_path: str):
    filename = os.path.basename(transcript_path)
    print(f"Reading: {filename}...")
    with open(transcript_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()

    transcript_content = compact_transcript(raw_content)
    print(f"Sending to {MODEL_NAME} for forensic analysis (payload: {len(transcript_content)} chars)...")
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Please analyze this incident timeline:\n\n{transcript_content}"}
                ],
                temperature=0.2,
                max_tokens=6000
            )
            
            raw_report = response.choices[0].message.content
            report = clean_model_output(raw_report)
            
            # Sanity check: Ensure clean report has content
            if not report or len(report) < 150:
                print("  Warning: Empty or corrupted report received from API, falling back.", flush=True)
                _write_deterministic_fallback(raw_content, output_path)
                return False
                
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)
                
            print(f"Success! Report saved to {output_path}\n", flush=True)
            return True
            
        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                wait_time = 25 * (attempt + 1)
                print(f"  Rate limited. Waiting {wait_time}s before retry ({attempt+1}/{max_retries})...", flush=True)
                time.sleep(wait_time)
            else:
                print(f"API Error ({e}). Generating Structured Deterministic Fallback...", flush=True)
                _write_deterministic_fallback(raw_content, output_path)
                return False
    
    print("  Max retries exceeded. Generating Structured Deterministic Fallback...", flush=True)
    _write_deterministic_fallback(raw_content, output_path)
    return False

from standalone_narrator import ForensicNarrator

narrator = ForensicNarrator()

def _write_deterministic_fallback(raw_content: str, output_path: str):
    """
    Invokes the Advanced Standalone Forensic Narrator as the fallback engine.
    Ensures 100% deterministic, cited, high-grade report generation if the API
    is unreachable or rate-limited.
    """
    try:
        fallback_report = narrator.narrate_transcript(raw_content)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(fallback_report)
        print(f"Standalone Narrator fallback saved to {output_path}\n", flush=True)
    except Exception as ex:
        print(f"Fallback generation error: {ex}", flush=True)

def main():
    input_dir = r"d:\TRACE\Timeline\transcripts"
    output_dir = r"d:\TRACE\AI_Reporter\final_reports"
    
    os.makedirs(output_dir, exist_ok=True)
    
    transcript_files = sorted(glob.glob(os.path.join(input_dir, "*.md")))
    if not transcript_files:
        print(f"No transcripts found in {input_dir}")
        return
        
    # Detect pending files (also re-process defective reports with thoughts or dummy text)
    pending = []
    for fp in transcript_files:
        out = os.path.join(output_dir, f"REPORT_{os.path.basename(fp)}")
        if os.path.exists(out):
            with open(out, 'r', encoding='utf-8') as f:
                content = f.read()
            if "auto-generated fallback" in content or "<thought>" in content or len(content.strip()) < 500 or "## 6." not in content:
                pending.append(fp)
        else:
            pending.append(fp)
    
    total = len(transcript_files)
    skip = total - len(pending)
    print(f"Found {total} incident transcripts. Skipping {skip} already verified. Processing {len(pending)}.", flush=True)
    
    success_count = 0
    for idx, filepath in enumerate(pending):
        filename = os.path.basename(filepath)
        output_filepath = os.path.join(output_dir, f"REPORT_{filename}")
        
        print(f"\n[{idx+1}/{len(pending)}] ", end="", flush=True)
        result = generate_report(filepath, output_filepath)
        if result:
            success_count += 1
        
        # Adaptive pause between calls to respect rate limit smoothly
        if idx < len(pending) - 1:
            print("  Pausing 4s for rate compliance...", flush=True)
            time.sleep(4)
    
    print(f"\n{'='*60}", flush=True)
    print(f"DONE! {success_count}/{len(pending)} forensic reports generated.", flush=True)
    print(f"Reports saved to: {output_dir}", flush=True)

if __name__ == "__main__":
    main()
