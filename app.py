import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from agents.data_agent import analyze_finances
from agents.advisor_agent import generate_advice
from agents.investment_agent import suggest_investments
from agents.coach_agent import build_coaching_plan
from utils.memory import get_user_profile, save_user_profile


# Streamlit page config
st.set_page_config(page_title="FinAI – Personal Finance Coach", layout="wide")

st.title("💸 FinAI – Multi-Agent Personal Finance Coach")

st.write(
    "Enter your monthly details and loan info. "
    "FinAI's agents will analyze your situation and build a step-by-step plan."
)

# --- Sidebar: user profile (simple memory) ---
st.sidebar.header("User Profile")
user_id = st.sidebar.text_input("User ID (for saving progress)", value="default")
load_btn = st.sidebar.button("Load last profile")

profile = get_user_profile(user_id) if load_btn else {}

# --- Main form: Income & expenses ---
st.subheader("1️⃣ Income & Expenses")

col1, col2 = st.columns(2)

with col1:
    income = st.number_input(
        "Monthly income",
        min_value=0.0,
        value=float(profile.get("income", 2200.0)),
        step=100.0,
    )
    rent = st.number_input(
        "Rent / Housing",
        min_value=0.0,
        value=float(profile.get("rent", 500.0)),
        step=50.0,
    )
    transport = st.number_input(
        "Transport",
        min_value=0.0,
        value=float(profile.get("transport", 200.0)),
        step=25.0,
    )

with col2:
    food = st.number_input(
        "Food & groceries",
        min_value=0.0,
        value=float(profile.get("food", 200.0)),
        step=25.0,
    )
    other = st.number_input(
        "Other fixed expenses",
        min_value=0.0,
        value=float(profile.get("other", 150.0)),
        step=25.0,
    )

# --- Loan details ---
st.subheader("2️⃣ Loan Details")

col3, col4 = st.columns(2)
with col3:
    loan_amount = st.number_input(
        "Total loan amount remaining",
        min_value=0.0,
        value=float(profile.get("loan_amount", 53600.0)),
        step=1000.0,
    )
with col4:
    interest_rate = st.number_input(
        "Annual interest rate (%)",
        min_value=0.0,
        value=float(profile.get("interest_rate", 11.5)),
        step=0.1,
    )

years = st.slider(
    "Loan payoff horizon (years)",
    min_value=1,
    max_value=20,
    value=int(profile.get("tenure_years", 10)),
)

# --- Run analysis button ---
if st.button("🚀 Run FinAI Analysis"):
    with st.spinner("Running multi-agent analysis..."):
        # 1) Data agent → numeric summary
        inputs = {
            "income": income,
            "rent": rent,
            "transport": transport,
            "food": food,
            "other": other,
            "loan_amount": loan_amount,
            "interest_rate": interest_rate,
            "years": float(years),
        }
        budget = analyze_finances(inputs)

        # Save profile to memory
        save_user_profile(user_id, budget)

        # 2) Advisor agent → text advice
        advisor_text = generate_advice(budget)

        # 3) Investment agent → suggestions
        investment_text = suggest_investments(budget)

        # 4) Coach agent → final plan
        coaching_plan = build_coaching_plan(budget, advisor_text, investment_text)

    # --- Show results ---
    st.success("Analysis complete! 🎉")

    # Numeric summary
    st.markdown("### 3️⃣ Budget Summary")
    st.write(budget)

    # Chart: Monthly allocation
    st.markdown("#### Monthly Allocation")

    chart_data = pd.DataFrame(
        {
            "category": ["Rent", "Transport", "Food", "Other", "EMI", "Savings"],
            "amount": [
                budget["rent"],
                budget["transport"],
                budget["food"],
                budget["other"],
                budget["emi"],
                budget["savings"],
            ],
        }
    )

    fig, ax = plt.subplots()
    ax.bar(chart_data["category"], chart_data["amount"])
    ax.set_ylabel("Amount")
    plt.xticks(rotation=30)
    st.pyplot(fig)

    # Advisor text
    st.markdown("### 4️⃣ Advisor Agent – Budget Feedback")
    st.write(advisor_text)

    # Investment text
    st.markdown("### 5️⃣ Investment Agent – Safe Plan")
    st.write(investment_text)

    # Final coaching plan
    st.markdown("### 6️⃣ Coach Agent – Your Personal Plan")
    st.write(coaching_plan)

else:
    st.info("Fill in your details and click **Run FinAI Analysis** to see your plan.")
