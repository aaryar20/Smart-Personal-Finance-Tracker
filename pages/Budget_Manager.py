import streamlit as st
import pandas as pd

from utils import load_transactions, load_budget, save_budget
from config import CURRENCY
from components.sidebar import build_sidebar


# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="Budget Manager",
    page_icon="💵",
    layout="wide"
)
build_sidebar()
st.title("💵 Monthly Budget Manager")
st.caption("Set your monthly budget and monitor your spending.")

# ---------------------------------------
# Load Budget
# ---------------------------------------

budget_df = load_budget()

if budget_df.empty:
    current_budget = 0.0
else:
    current_budget = float(budget_df.iloc[0]["monthly_budget"])

# ---------------------------------------
# Budget Input
# ---------------------------------------

st.subheader("Set Monthly Budget")

budget = st.number_input(
    f"Monthly Budget ({CURRENCY})",
    min_value=0.0,
    value=current_budget,
    step=100.0
)

if st.button("💾 Save Budget", use_container_width=True):

    save_budget(budget)

    st.success("Budget saved successfully!")

    current_budget = budget

# ---------------------------------------
# Load Transactions
# ---------------------------------------

df = load_transactions()

expense = 0.0

if not df.empty:

    expense = (
        df[df["type"] == "Expense"]["amount"]
        .sum()
    )

remaining = max(
    current_budget-expense,
    0
)

# ---------------------------------------
# Summary Cards
# ---------------------------------------

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric(
    "🎯 Budget",
    f"{CURRENCY}{current_budget:,.2f}"
)

col2.metric(
    "💸 Expenses",
    f"{CURRENCY}{expense:,.2f}"
)

col3.metric(
    "💰 Remaining",
    f"{CURRENCY}{remaining:,.2f}"
)

st.divider()

# ---------------------------------------
# Progress Bar
# ---------------------------------------

if current_budget > 0:

    progress = expense / current_budget

    progress = min(progress, 1.0)

    st.subheader("Budget Usage")

    st.progress(progress)

    st.write(
        f"Spent **{CURRENCY}{expense:,.2f}** out of **{CURRENCY}{current_budget:,.2f}**"
    )

    st.write(
        f"Budget Used: **{expense/current_budget*100:.1f}%**"
    )

# ---------------------------------------
# Alerts
# ---------------------------------------

if current_budget > 0:

    if expense > current_budget:

        st.error("⚠️ You have exceeded your monthly budget.")

    elif expense >= current_budget * 0.8:

        st.warning("⚠️ You have used more than 80% of your monthly budget.")

    else:

        st.success("✅ Your spending is within budget.")

else:

    st.info("Set a monthly budget to begin tracking.")