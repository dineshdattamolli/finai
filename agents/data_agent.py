from typing import Dict, Any
from utils.finance_math import calc_emi, build_budget


def analyze_finances(inputs: Dict[str, float]) -> Dict[str, Any]:
    """
    Data-focused agent: computes EMI and builds a monthly budget summary.
    No LLM calls here—just pure logic.
    """
    income = inputs["income"]
    rent = inputs["rent"]
    transport = inputs["transport"]
    food = inputs["food"]
    other = inputs["other"]
    principal = inputs["loan_amount"]
    rate = inputs["interest_rate"]
    years = inputs["years"]

    emi = calc_emi(principal, rate, years)
    budget = build_budget(income, rent, transport, food, other, emi)

    budget["tenure_years"] = years
    budget["loan_amount"] = principal
    budget["interest_rate"] = rate

    return budget
