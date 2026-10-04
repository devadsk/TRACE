"""
Stage 5 (real version) — LLM-generated narrative with verify-and-retry,
checkpointing, and automatic rate-limit backoff.
"""

import os
import re
import json
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

MODEL = "openai/gpt-oss-20b"
MAX_RETRIES = 2
RESULTS_PATH = "results/narratives_llm.jsonl"   # JSON Lines — one object per line

client = Groq(api_key=os.environ["GROQ_API_KEY"])

SYSTEM_PROMPT = """You write short, factual incident narratives for an aerospace \
log-analysis tool. You will be given a JSON object describing ONE incident, \
already computed by a separate deterministic pipeline (you did not see any \
raw logs). Write exactly one paragraph, in plain English, describing what \
happened. Rules:
- Only state facts present in the JSON you were given. Never infer or add anything.
- You MUST cite evidence using the exact IDs given in "evidence_ids", formatted as #ID.
- Cite EVERY id in "evidence_ids" at least once, and NEVER cite any id not in that list.
- State the confidence level and whether it was resolved, using the given fields.
- Do not use markdown. Output only the paragraph, nothing else."""

def build_user_prompt(incident: dict) -> str:
    return f"Incident data:\n{json.dumps(incident, indent=2)}\n\nWrite the narrative."

def extract_citations(text: str) -> set:
    return set(re.findall(r"#(\w+)", text))

def verify(text: str, valid_ids: set):
    cited = extract_citations(text)
    bad = cited - valid_ids
    missing = valid_ids - cited
    return (not bad and not missing), bad, missing

def load_done_ids():
    """Read existing progress file, return the set of incident_ids already completed."""
    done = set()
    if os.path.exists(RESULTS_PATH):
        with open(RESULTS_PATH) as f:
            for line in f:
                if line.strip():
                    done.add(json.loads(line)["incident_id"])
    return done

def append_result(result: dict):
    os.makedirs("results", exist_ok=True)
    with open(RESULTS_PATH, "a") as f:
        f.write(json.dumps(result) + "\n")

def call_with_backoff(messages, max_wait_retries=5):
    """Calls the API; on a rate-limit error, sleeps and retries automatically."""
    for i in range(max_wait_retries):
        try:
            return client.chat.completions.create(
                model=MODEL,
                max_tokens=1200,
                temperature=0.3,
                reasoning_effort="low",
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
            )
        except Exception as e:
            msg = str(e)
            if "rate_limit" in msg or "429" in msg:
                # try to parse "try again in Xm Ys" from the error message
                m = re.search(r"try again in (?:(\d+)m)?(?:([\d.]+)s)?", msg)
                wait_s = 60
                if m:
                    mins = float(m.group(1) or 0)
                    secs = float(m.group(2) or 0)
                    wait_s = mins * 60 + secs + 5   # +5s buffer
                print(f"  Rate limited. Waiting {wait_s:.0f}s before retrying...")
                time.sleep(wait_s)
            else:
                raise
    raise RuntimeError("Exceeded max wait retries for rate limiting")

def narrate_incident_llm(incident: dict) -> dict:
    valid_ids = set(incident["evidence_ids"])
    messages = [{"role": "user", "content": build_user_prompt(incident)}]

    text = ""
    for attempt in range(1, MAX_RETRIES + 2):
        response = call_with_backoff(messages)
        text = response.choices[0].message.content.strip()
        ok, bad, missing = verify(text, valid_ids)

        if ok:
            return {"incident_id": incident["incident_id"], "narrative": text,
                     "verified": True, "attempts": attempt}

        problems = []
        if bad:
            problems.append(f"You cited these IDs which do NOT exist: {sorted(bad)}.")
        if missing:
            problems.append(f"You forgot to cite these required IDs: {sorted(missing)}.")
        correction = (
            "Your previous answer failed verification. " + " ".join(problems) +
            " Rewrite the paragraph, citing ONLY and ALL of: " +
            ", ".join(f"#{i}" for i in valid_ids)
        )
        messages.append({"role": "assistant", "content": text})
        messages.append({"role": "user", "content": correction})

    return {"incident_id": incident["incident_id"], "narrative": text,
             "verified": False, "attempts": MAX_RETRIES + 1}


if __name__ == "__main__":
    with open("results/incidents.json") as f:
        incidents = json.load(f)

    done_ids = load_done_ids()
    print(f"Already completed: {len(done_ids)} / {len(incidents)}")

    remaining = [i for i in incidents if i["incident_id"] not in done_ids]
    print(f"Remaining to process: {len(remaining)}\n")

    for inc in remaining:
        result = narrate_incident_llm(inc)
        append_result(result)   # <-- saved immediately, not at the end
        print(f"[{result['incident_id']}] verified={result['verified']} "
              f"attempts={result['attempts']}")
        print(f"  {result['narrative']}\n")

    # Final tally from the full file
    all_results = []
    with open(RESULTS_PATH) as f:
        for line in f:
            if line.strip():
                all_results.append(json.loads(line))
    passed = sum(1 for r in all_results if r["verified"])
    print(f"\n{passed}/{len(all_results)} total narratives verified")