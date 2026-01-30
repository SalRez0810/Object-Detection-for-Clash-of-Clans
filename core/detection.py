def run_predict(model, frame, conf, iou, imgsz, tracking=True):
    if tracking:
        return model.track(
            frame,
            persist=True,
            conf=conf,
            iou=iou,
            imgsz=imgsz
        )
    return model.predict(
        frame,
        conf=conf,
        iou=iou,
        imgsz=imgsz
    )
