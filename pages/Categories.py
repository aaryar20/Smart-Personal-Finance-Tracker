import streamlit as st

from components.sidebar import build_sidebar
from utils import (
    load_categories,
    add_category,
    delete_category
)

st.set_page_config(
    page_title="Categories",
    page_icon="🏷️",
    layout="wide"
)

build_sidebar()

st.title("🏷️ Category Manager")

st.write(
    "Manage the categories used throughout the application."
)

st.divider()

# -----------------------------
# Add Category
# -----------------------------

st.subheader("➕ Add Category")

new_category = st.text_input("Category Name")

if st.button("Add Category"):

    if new_category.strip():

        add_category(new_category.strip())

        st.success("Category added successfully.")

        st.rerun()

st.divider()

# -----------------------------
# Existing Categories
# -----------------------------

st.subheader("📂 Existing Categories")

categories = load_categories()

for category in categories:

    left, right = st.columns([5,1])

    with left:

        st.write(category)

    with right:

        if st.button(
            "🗑",
            key=category
        ):

            delete_category(category)

            st.success("Category deleted.")

            st.rerun()