import streamlit as st

def show_header():
    st.markdown("""
    <div class="header-card">
        <h1>Clash of Clans Object Detection</h1>
        <p>Powered by YOLOv11 — Real-time Detection & Tracking</p>
    </div>
    """, unsafe_allow_html=True)
