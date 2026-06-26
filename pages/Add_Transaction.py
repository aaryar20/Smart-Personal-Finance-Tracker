import streamlit as st
from datetime import date

from utils import add_transaction
from config import CURRENCY
from components.sidebar import build_sidebar

st.set_page_config(
    page_title="Add Transaction",
    page_icon="➕",
    layout="wide"
)

build_sidebar()

st.title("➕ Add New Transaction")
st.write("Fill in the details below and click **Save Transaction**.")

col1, col2 = st.columns(2)

with col1:
    transaction_date = st.date_input(
        "Date",
        value=date.today()
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        ["Expense", "Income"]
    )

with col2:
    from utils import load_categories
    categories = load_categories()
    category = st.selectbox("Category",
                            categories)

    amount = st.number_input(
        f"Amount ({CURRENCY})",
        min_value=0.0,
        step=1.0
    )

description = st.text_area(
    "Description (Optional)"
)

st.write("")

if st.button("💾 Save Transaction", use_container_width=True):

    if amount <= 0:
        st.error("Amount must be greater than 0.")

    else:

        add_transaction(
            str(transaction_date),
            transaction_type,
            category,
            amount,
            description
        )

        st.success("Transaction added successfully!")

        st.balloons()