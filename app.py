import streamlit as st
import cv2
import numpy as np
import tempfile
import uuid
import os

from ui.styles import load_css
from ui.header import show_header
from ui.sidebar import sidebar_settings
from core.model_loader import load_yolo_model
from core.detection import run_predict
from core.drawing import draw_annotations

st.set_page_config("CoC YOLO Detector", layout="wide")
load_css()
show_header()

model_name, conf, iou, imgsz, tracking, color_by_id = sidebar_settings()

model = load_yolo_model(f"models/{model_name}")
model_names = model.names

tab_img, tab_vid = st.tabs(["Image Detection", "Video Detection"])

# ================= IMAGE =================
with tab_img:
    img_file = st.file_uploader("Upload Image", ["jpg","png","jpeg"])
    if img_file:
        img = cv2.imdecode(
            np.frombuffer(img_file.read(), np.uint8),
            cv2.IMREAD_COLOR
        )
        results = model.predict(img, conf=conf, iou=iou, imgsz=imgsz)[0]
        annotated = draw_annotations(img, results, model_names, color_by_id)
        st.image(annotated, channels="BGR", use_column_width=True)

# ================= VIDEO =================
with tab_vid:
    vid_file = st.file_uploader("Upload Video", ["mp4","avi","mkv"])
    if vid_file:
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp.write(vid_file.read())
        cap = cv2.VideoCapture(tmp.name)

        frame_box = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = run_predict(
                model, frame, conf, iou, imgsz, tracking
            )[0]

            annotated = draw_annotations(
                frame, results, model_names, color_by_id
            )
            frame_box.image(annotated, channels="BGR")

        cap.release()