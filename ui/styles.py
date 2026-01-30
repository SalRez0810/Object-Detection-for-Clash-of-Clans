import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg,#fbfdff,#f6f9ff);
    }
    .header-card {
        background: linear-gradient(135deg,#667eea,#764ba2);
        color:white;
        border-radius:14px;
        padding:28px;
        margin-bottom:18px;
    }
    </style>
    """, unsafe_allow_html=True)
