import os
from dotenv import load_dotenv
import requests

load_dotenv(override=True)
key = os.getenv("GROQ_API_KEY", "")

res = requests.post(
    'https://api.groq.com/openai/v1/chat/completions', 
    headers={'Authorization': f'Bearer {key}'},
    json={'model': 'openai/gpt-oss-20b', 'messages': [{'role': 'user', 'content': 'test'}]}
)
print(res.status_code)
print(res.text)
