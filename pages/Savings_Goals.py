import streamlit as st

from components.sidebar import build_sidebar
from utils import load_goal, save_goal
from config import CURRENCY

st.set_page_config(
    page_title="Savings Goals",
    page_icon="🎯",
    layout="wide"
)

build_sidebar()

st.title("🎯 Savings Goals")

goal_df = load_goal()

if goal_df.empty:

    goal_name = ""
    target = 0.0
    current = 0.0

else:

    goal_name = goal_df.iloc[0]["goal_name"]
    target = goal_df.iloc[0]["target_amount"]
    current = goal_df.iloc[0]["current_amount"]

st.subheader("Goal Details")

goal_name = st.text_input(
    "Goal Name",
    value=goal_name
)

target = st.number_input(
    "Target Amount",
    value=float(target),
    min_value=0.0
)

current = st.number_input(
    "Current Savings",
    value=float(current),
    min_value=0.0
)

if st.button("Save Goal"):

    save_goal(
        goal_name,
        target,
        current
    )

    st.success("Goal saved successfully.")

    st.rerun()

st.divider()

if target > 0:

    progress = current / target

    progress = min(progress,1.0)

    st.subheader("Progress")

    st.progress(progress)

    st.metric(
        "Completion",
        f"{progress*100:.1f}%"
    )

    remaining = target-current

    st.metric(
        "Remaining",
        f"{CURRENCY}{remaining:,.2f}"
    )