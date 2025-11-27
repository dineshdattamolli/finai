from typing import Dict, Any
from models.openai_client import chat_completion

SYSTEM_PROMPT = """
You are 'FinAI', a warm, structured personal finance coach.
You will receive:
1) Numeric analysis of the user's finances
2) Advisor's budget optimization notes
3) Investment suggestions

Your job:
- Combine everything into ONE clear, motivating plan
- Structure with short sections and bullet points:
  - TL;DR
  - This is your current situation
  - What to do this month
  - What to do in next 6–12 months
- Very practical, no jargon.
Max 300 words.
"""


def build_coaching_plan(
    budget: Dict[str, Any],
    advisor_text: str,
    investment_text: str,
) -> str:
    """
    Final orchestration agent: merges numeric data + advisory text
    into one final coaching message.
    """
    user_prompt = f"""
[NUMERIC BUDGET DATA]
{budget}

[ADVISOR NOTES]
{advisor_text}

[INVESTMENT NOTES]
{investment_text}

Now create the final coaching plan as described.
"""
    return chat_completion(SYSTEM_PROMPT, user_prompt)
