import streamlit as st


def show_transaction(row):

    icon = "💸" if row.type == "Expense" else "💰"

    with st.container(border=True):

        c1, c2 = st.columns([5, 1])

        with c1:

            st.markdown(f"### {icon} {row.category}")

            st.caption(row.date)

            st.write(f"**Amount:** ₹{row.amount:,.2f}")

            if row.description:
                st.write(row.description)

        with c2:

            edit = st.button(
                "✏️",
                key=f"edit_{row.id}"
            )

            delete = st.button(
                "🗑",
                key=f"delete_{row.id}"
            )

        return edit, delete