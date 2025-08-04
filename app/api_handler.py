import os
from openai import OpenAI

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "deepseek/deepseek-r1-0528:free"

class APIError(Exception):
    pass

def generate_reply_api(email, tone, intent):
    if not OPENROUTER_API_KEY:
        raise APIError("OpenRouter API key not set.")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )
    prompt = f"Received Email:\n{email}\n\nReply Tone: {tone}\nIntent: {intent}\n\nGenerate a context-aware reply."
    try:
        completion = client.chat.completions.create(
            extra_headers={
                # Optionally set these for rankings
                # "HTTP-Referer": "<YOUR_SITE_URL>",
                # "X-Title": "<YOUR_SITE_NAME>",
            },
            extra_body={},
            model=MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise APIError(f"API Error: {str(e)}")
