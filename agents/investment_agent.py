from typing import Dict, Any
from models.openai_client import chat_completion

SYSTEM_PROMPT = """
You are a conservative investment coach.
The user is a young professional with limited savings and possibly student/education loans.
Your goal:
- Focus first on emergency fund and debt repayment
- Then suggest simple, low-risk, long-term investments (index funds, etc.)
Do NOT give specific stock tickers.
Use simple English and concrete monthly rupee/dollar amounts.
Max 200 words.
"""


def suggest_investments(budget: Dict[str, Any]) -> str:
    """
    Use the LLM to suggest a safe, high-level investment and savings strategy.
    """
    user_prompt = (
        "User's current financial snapshot:\n"
        f"{budget}\n\n"
        "Suggest a safe plan for:\n"
        "- Emergency fund building\n"
        "- Debt repayment priority\n"
        "- Basic long-term investing allocation.\n"
        "User is okay with small, consistent monthly investing."
    )
    return chat_completion(SYSTEM_PROMPT, user_prompt)
