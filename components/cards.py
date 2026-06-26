import streamlit as st
import streamlit as st


def metric_card(title, value, help_text=None):
    st.metric(
        label=title,
        value=value,
        help=help_text
    )


def metric_card(title, value, icon, help_text=None):

    with st.container(border=True):

        col1, col2 = st.columns([1, 4])

        with col1:
            st.markdown(
                f"<h1 style='text-align:center'>{icon}</h1>",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <h5 style="margin-bottom:0px;">
                {title}
                </h5>

                <h2 style="margin-top:0px;">
                {value}
                </h2>
                """,
                unsafe_allow_html=True
            )

        if help_text:
            st.caption(help_text)