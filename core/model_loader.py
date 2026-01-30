import streamlit as st
from ultralytics import YOLO

@st.cache_resource
def load_yolo_model(path):
    return YOLO(path)
