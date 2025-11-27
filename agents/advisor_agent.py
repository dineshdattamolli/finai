from typing import Dict, Any
from models.openai_client import chat_completion


SYSTEM_PROMPT = """
You are a helpful personal finance advisor.
You will receive a structured dictionary of a user's monthly budget and loan details.
Explain in simple, concrete language:
- How healthy this budget is
- Which 2-3 biggest issues to fix
- Exact actionable steps (with numbers) for the next month.
Keep it under 250 words. Be friendly but honest.
"""


def generate_advice(budget: Dict[str, Any]) -> str:
    """
    Use the LLM to turn numeric budget data into human-readable advice.
    """
    user_prompt = (
        "Here is the user's budget data (Python dict):\n"
        f"{budget}\n\n"
        "Give advice as bullet points, then a 2-3 line summary."
    )
    return chat_completion(SYSTEM_PROMPT, user_prompt)
