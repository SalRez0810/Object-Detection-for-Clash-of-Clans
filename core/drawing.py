import cv2
from utils.bbox_utils import to_int_bbox, get_box_id, color_for_id

def format_label(cls_id, names):
    if names and cls_id in names:
        return names[cls_id].replace("_", " ").title()
    return str(cls_id)


def draw_annotations(frame, results, model_names, color_by_id=True):
    img = frame.copy()

    if results is None:
        return img

    for box in results.boxes:
        x1, y1, x2, y2 = to_int_bbox(box)
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = f"{format_label(cls_id, model_names)} ({conf:.2f})"

        tid = get_box_id(box)
        color = color_for_id(tid) if color_by_id else (0,255,0)

        cv2.rectangle(img, (x1,y1), (x2,y2), color, 2)
        (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        cv2.rectangle(img, (x1, y1-th-8), (x1+tw+4, y1), color, -1)
        cv2.putText(img, label, (x1+2, y1-6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)

    return img
