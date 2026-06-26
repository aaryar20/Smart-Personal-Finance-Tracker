import streamlit as st
import pandas as pd

from utils import (
    load_transactions,
    delete_transaction,
    load_categories
)
from config import CURRENCY
from components.sidebar import build_sidebar


st.set_page_config(
    page_title="Transaction History",
    page_icon="📜",
    layout="wide"
)
build_sidebar()
st.title("📜 Transaction History")
CATEGORY_ICONS = {
    "Food": "🍔",
    "Transport": "🚗",
    "Shopping": "🛍️",
    "Entertainment": "🎬",
    "Bills": "🧾",
    "Healthcare": "🏥",
    "Education": "🎓",
    "Salary": "💼",
    "Freelance": "💻",
    "Investment": "📈",
    "Other": "📦"
}

df = load_transactions()

df["date"] = pd.to_datetime(df["date"])
if df.empty:
    st.info("No transactions available.")
    st.stop()

st.subheader("📈 Transaction Summary")

col1, col2, col3, col4 = st.columns(4)

income = df[df["type"] == "Income"]["amount"].sum()
expense = df[df["type"] == "Expense"]["amount"].sum()

col1.metric("Transactions", len(df))
col2.metric("Income", f"{CURRENCY}{income:,.2f}")
col3.metric("Expense", f"{CURRENCY}{expense:,.2f}")
col4.metric("Balance", f"{CURRENCY}{income-expense:,.2f}")

st.divider()

# -----------------------
# Search
# -----------------------

search = st.text_input(
    "🔍 Search by Category or Description"
)

if search:

    df = df[
        df["category"].str.contains(search, case=False, na=False)
        |
        df["description"].fillna("").str.contains(search, case=False, na=False)
    ]

# -----------------------
# Filter
# -----------------------

transaction_filter = st.selectbox(
    "Filter",
    ["All", "Income", "Expense"]
)

if transaction_filter != "All":
    df = df[df["type"] == transaction_filter]
categories = ["All"] + load_categories()

selected_category = st.selectbox(
    "Category",
    categories
)

if selected_category != "All":
    df = df[df["category"] == selected_category]

# -----------------------
# Date Filter
# -----------------------

if df.empty:
    st.warning("No transactions match the selected filters.")
    st.stop()

st.subheader("📅 Date Range")

col1, col2 = st.columns(2)

min_date = df["date"].min().date()
max_date = df["date"].max().date()

with col1:
    start_date = st.date_input(
        "Start Date",
        value=min_date,
        min_value=min_date,
        max_value=max_date
    )

with col2:
    end_date = st.date_input(
        "End Date",
        value=max_date,
        min_value=min_date,
        max_value=max_date
    )

df = df[
    (df["date"] >= pd.Timestamp(start_date))
    &
    (df["date"] <= pd.Timestamp(end_date))
]

# -----------------------
# Sort
# -----------------------

sort_order = st.radio(
    "Sort",
    ["Newest First", "Oldest First"],
    horizontal=True
)

ascending = sort_order == "Oldest First"

df = df.sort_values(
    "date",
    ascending=ascending
)

# -----------------------
# Display Cards
# -----------------------

for row in df.itertuples():

    with st.container(border=True):

        left, right = st.columns([6,1])

        with left:
            icon = CATEGORY_ICONS.get(row.category, "📦")
            description = row.description if row.description else "No description"

            st.markdown(
                f"""
### {icon} {row.category}

**Date:** {row.date}

**Type:** {row.type}

**Amount:** {CURRENCY}{row.amount:,.2f}

**Description:** {description}
"""
            )

        with right:

            st.write("")

            if st.button(
                 "🗑 Delete",
                 key=f"delete_{row.id}"
                 ):
                st.session_state["delete_id"] = row.id
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Yes, Delete"):
                            delete_transaction(
                                st.session_state["delete_id"]
                                )
                            del st.session_state["delete_id"]
                            st.success("Transaction deleted successfully.")
                            st.rerun()
                            with col2:
                                if st.button("Cancel"):
                                    del st.session_state["delete_id"]
                                    st.rerun()

if "delete_id" in st.session_state:

    st.warning("Are you sure you want to delete this transaction?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes, Delete"):

            delete_transaction(
                st.session_state["delete_id"]
            )

            del st.session_state["delete_id"]

            st.success("Transaction deleted successfully.")

            st.rerun()

    with col2:
        if st.button("Cancel"):

            del st.session_state["delete_id"]

            st.rerun()