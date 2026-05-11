import streamlit as st


def remove_vertical_gap():
    """Force removes the standard Streamlit block spacing."""
    st.markdown("""
        <style>
        [data-testid="stVerticalBlock"] {
            gap: 0rem !important;
        }
        </style>
    """, unsafe_allow_html=True)