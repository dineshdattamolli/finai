import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not set in .env")

# Create OpenAI client
client = OpenAI(api_key=api_key)


def chat_completion(system_prompt: str, user_prompt: str) -> str:
    """
    Helper to send a chat completion request with a system + user prompt.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # you can upgrade this if you want
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content
