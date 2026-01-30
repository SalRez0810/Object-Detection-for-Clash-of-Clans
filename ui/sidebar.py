import streamlit as st
from utils.file_utils import list_models

def sidebar_settings():
    st.sidebar.header("Settings")

    models = list_models("models")
    model = st.sidebar.selectbox("Select Model", models)

    conf = st.sidebar.slider("Confidence", 0.05, 0.99, 0.25, 0.01)
    iou = st.sidebar.slider("IoU", 0.0, 1.0, 0.45, 0.01)
    imgsz = st.sidebar.selectbox("Image Size", [320,480,640,960], index=2)

    tracking = st.sidebar.checkbox("Enable Tracking", True)
    color_by_id = st.sidebar.checkbox("Color by Track ID", True)

    return model, conf, iou, imgsz, tracking, color_by_id
