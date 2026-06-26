import streamlit as st

st.set_page_config(
    page_title="Smart Finance Tracker",
    page_icon="💰",
    layout="wide"
)

st.sidebar.title("💼 Finance Tracker")
st.sidebar.success("Manage your finances efficiently!")

st.sidebar.markdown("---")

st.sidebar.write("Developed using")

st.sidebar.write("• Python")
st.sidebar.write("• Streamlit")
st.sidebar.write("• SQLite")
st.sidebar.write("• Plotly")

st.title("💰 Smart Expense & Finance Tracker")

st.write("""
Welcome!

Use the navigation menu on the left to:

- ➕ Add Transactions
- 📊 View Dashboard
- 📜 View Transaction History
- 💵 Manage Budget
- 📄 Download Reports
""")