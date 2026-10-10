import os
from dotenv import load_dotenv
import requests

load_dotenv(override=True)
key = os.getenv("GROQ_API_KEY")
print(f"Key loaded: {key[:10]}...")

res = requests.get('https://api.groq.com/openai/v1/models', headers={'Authorization': f'Bearer {key}'})
print("Response:", res.status_code)
print(res.text)
