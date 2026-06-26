import streamlit as st
import pandas as pd
import plotly.express as px


from utils import load_transactions, load_budget, load_categories, load_goal
from config import CURRENCY
from components.sidebar import build_sidebar

from components.cards import metric_card
from components.charts import expense_line, expense_pie
from components.sidebar import build_sidebar


goal_df = load_goal()

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)
build_sidebar()
st.markdown("""
# 💰 Smart Finance Tracker

Welcome back!

Here's your financial overview.
""")
st.caption("Monitor your income, expenses and budget.")

# -----------------------------
# Load Data
# -----------------------------
df = load_transactions()
budget_df = load_budget()

if df.empty:
    st.info("No transactions found.")
    st.stop()

# -----------------------------
# Data Preparation
# -----------------------------
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

income_df = df[df["type"] == "Income"]
expense_df = df[df["type"] == "Expense"]

income = income_df["amount"].sum()
expense = expense_df["amount"].sum()
balance = income - expense
transactions = len(df)

# -----------------------------
# Summary Cards
# -----------------------------
st.subheader("📈 Financial Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "💰 Income",
        f"{CURRENCY}{income:,.2f}"
    )

with c2:
    st.metric(
        "💸 Expense",
        f"{CURRENCY}{expense:,.2f}"
    )

with c3:
    st.metric(
        "🏦 Balance",
        f"{CURRENCY}{balance:,.2f}"
    )

with c4:
    st.metric(
        "📋 Transactions",
        f"{len(df)}"
    )

st.divider()

st.subheader("🏆 Financial Health Score")

score = 100

if expense > income:
    score -= 40

if expense >= income * 0.8:
    score -= 20

if balance <= 0:
    score -= 20

if score >= 90:
    color = "🟢 Excellent"

elif score >= 70:
    color = "🟡 Good"

elif score >= 50:
    color = "🟠 Fair"

else:
    color = "🔴 Poor"

st.metric(
    "Score",
    f"{score}/100"
)

st.write(color)

st.subheader("⚡ Quick Insights")

left, right = st.columns(2)

with left:

    avg_expense = (
        expense_df["amount"].mean()
        if not expense_df.empty else 0
    )

    highest = (
        expense_df["amount"].max()
        if not expense_df.empty else 0
    )

    st.info(f"Average Expense: {CURRENCY}{avg_expense:,.2f}")

    st.info(f"Highest Expense: {CURRENCY}{highest:,.2f}")

with right:

    if not expense_df.empty:

        top_category = (
            expense_df.groupby("category")["amount"]
            .sum()
            .idxmax()
        )

        st.success(f"Highest Spending Category: {top_category}")

    st.success(f"Transactions Recorded: {len(df)}")

# -----------------------------
# Charts
# -----------------------------
left, right = st.columns([2, 1])

with left:

    st.subheader("📈 Spending Trend")

    if expense_df.empty:
        st.info("No expense data available.")
    else:

        trend = (
            expense_df
            .groupby("date", as_index=False)["amount"]
            .sum())

        fig = px.line(
            trend,
            x="date",
            y="amount",
            markers=True
        )

        st.plotly_chart(
            expense_line(trend),
            use_container_width=True)

with right:

    st.subheader("🥧 Expense Breakdown")

    if expense_df.empty:
        st.info("No expense data available.")
    else:

        pie = px.pie(
            expense_df,
            names="category",
            values="amount",
            hole=0.55
        )

        pie.update_traces(
            textposition="inside",
            textinfo="percent+label"
        )

        st.plotly_chart(
            expense_pie(expense_df),
            use_container_width=True)

st.divider()

st.subheader("📅 Monthly Expense Analysis")

monthly = (
    expense_df
    .groupby(expense_df["date"].dt.to_period("M"))["amount"]
    .sum()
    .reset_index()
)

monthly["date"] = monthly["date"].astype(str)

fig = px.bar(
    monthly,
    x="date",
    y="amount",
    title="Monthly Expenses"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("📊 Income vs Expense")

comparison = pd.DataFrame({
    "Type": ["Income", "Expense"],
    "Amount": [income, expense]
})

fig = px.bar(
    comparison,
    x="Type",
    y="Amount",
    text="Amount"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("🏆 Top Spending Categories")

top_categories = (
    expense_df
    .groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

st.dataframe(
    top_categories,
    use_container_width=True,
    hide_index=True
)

expense_df["weekday"] = expense_df["date"].dt.day_name()

weekday = (
    expense_df
    .groupby("weekday")["amount"]
    .sum()
    .reindex([
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ])
    .reset_index()
)

fig = px.bar(
    weekday,
    x="weekday",
    y="amount",
    title="Spending by Weekday"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

daily = (
    expense_df
    .groupby("date")["amount"]
    .sum()
)

if not daily.empty:

    highest_day = daily.idxmax()
    highest_amount = daily.max()

    st.info(
        f"📅 Highest spending day: **{highest_day.date()}** ({CURRENCY}{highest_amount:,.2f})"
    )

st.divider()

st.subheader("📆 Monthly Summary")

summary = pd.DataFrame({
    "Income": [income],
    "Expense": [expense],
    "Balance": [balance]
})

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Top Categories
# -----------------------------
left, right = st.columns(2)

with left:

    st.subheader("🏆 Top Spending Categories")

    if expense_df.empty:
        st.info("No expense data available.")
    else:
        top = (
            expense_df
            .groupby("category", as_index=False)["amount"]
            .sum()
            .sort_values("amount",
                         ascending=False))

        st.dataframe(
            top,
            use_container_width=True,
            hide_index=True
        )

with right:

    st.subheader("📋 Recent Transactions")

    recent = (
        df.sort_values(
            "date",
            ascending=False
        ).head(5)
    )

    st.dataframe(
        recent,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# -----------------------------
# Budget Progress
# -----------------------------
st.divider()

st.subheader("🎯 Budget Progress")

if not budget_df.empty:

    budget = budget_df.iloc[0]["monthly_budget"]

    progress = min(expense / budget, 1.0) if budget > 0 else 0

    st.progress(progress)

    remaining = budget - expense

    c1, c2 = st.columns(2)

    c1.metric(
        "Budget",
        f"{CURRENCY}{budget:,.2f}"
    )

    c2.metric(
        "Remaining",
        f"{CURRENCY}{remaining:,.2f}"
    )

    if expense > budget:
        st.error("⚠ Budget exceeded")

    elif expense >= budget * 0.8:
        st.warning("⚠ 80% of budget used")

    else:
        st.success("✅ Budget is on track")

st.divider()

st.subheader("🕒 Recent Transactions")

recent = (
    df
    .sort_values("date", ascending=False)
    .head(5)
)

st.dataframe(
    recent[
        [
            "date",
            "category",
            "type",
            "amount"
        ]
    ],
    use_container_width=True,
    hide_index=True
)
st.subheader("📅 Dashboard Filters")

col1, col2 = st.columns(2)

with col1:
    metric_card(
        "💰 Income",
        f"{CURRENCY}{income:,.2f}")

with col2:
    category = st.selectbox(
        "Category",
        ["All"] + load_categories()
    )

if transaction_type != "All":
    df = df[df["type"] == transaction_type]

if category != "All":
    df = df[df["category"] == category]

st.divider()

st.subheader("💡 Smart Insights")

if expense > income:
    st.error("Your expenses are greater than your income.")

elif expense >= income * 0.8:
    st.warning("Your expenses are close to your income. Consider reducing discretionary spending.")

else:
    st.success("Your spending is healthy compared to your income.")

if not expense_df.empty:
    top_category = (
        expense_df
        .groupby("category")["amount"]
        .sum()
        .idxmax()
    )

    st.info(f"Your highest spending category is **{top_category}**.")

st.divider()

st.subheader("🎯 Savings Goal")

if not goal_df.empty:

    goal = goal_df.iloc[0]

    progress = goal["current_amount"] / goal["target_amount"]

    progress = min(progress,1.0)

    st.progress(progress)

    st.write(
        f"**{goal['goal_name']}**"
    )

    st.write(
        f"{CURRENCY}{goal['current_amount']:,.2f} / {CURRENCY}{goal['target_amount']:,.2f}"
    )