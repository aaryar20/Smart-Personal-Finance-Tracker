import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_transactions
from components.sidebar import build_sidebar
from components.exports import export_excel
from config import CURRENCY

df = load_transactions()
if st.button("📗 Export Excel"):

    export_excel(df)

    st.success("Excel report exported.")



st.title("📊 Financial Reports")

st.divider()

income = df[df["type"] == "Income"]["amount"].sum()
expense = df[df["type"] == "Expense"]["amount"].sum()

balance = income - expense

col1, col2, col3 = st.columns(3)

col1.metric("Income", f"₹{income:,.2f}")
col2.metric("Expense", f"₹{expense:,.2f}")
col3.metric("Balance", f"₹{balance:,.2f}")

st.divider()


category_summary = (
    df[df["type"] == "Expense"]
    .groupby("category")["amount"]
    .sum()
    .reset_index()
)

fig = px.bar(
    category_summary,
    x="category",
    y="amount",
    title="Expense by Category",
    text="amount"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

df["date"] = pd.to_datetime(df["date"])

monthly = (
    df.groupby(df["date"].dt.to_period("M"))["amount"]
    .sum()
    .reset_index()
)

monthly["date"] = monthly["date"].astype(str)

fig = px.line(
    monthly,
    x="date",
    y="amount",
    markers=True,
    title="Monthly Financial Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)
build_sidebar()
st.title("📄 Financial Reports")

df = load_transactions()

if df.empty:
    st.info("No transactions available.")
    st.stop()
df["date"] = pd.to_datetime(df["date"])
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download CSV Report",
    data=csv,
    file_name="finance_report.csv",
    mime="text/csv"
)
st.metric(
    "Transactions",
    len(df)
)
st.metric(
    "Total Income",
    f"₹{df[df['type']=='Income']['amount'].sum():,.2f}"
)
st.metric(
    "Total Expense",
    f"₹{df[df['type']=='Expense']['amount'].sum():,.2f}"
)