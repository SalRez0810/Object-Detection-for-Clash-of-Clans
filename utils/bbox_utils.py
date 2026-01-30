def to_int_bbox(box):
    try:
        arr = box.xyxy[0].cpu().numpy()
    except:
        arr = box.xyxy[0]
    return tuple(map(int, arr))


def get_box_id(box):
    if hasattr(box, "id") and box.id is not None:
        try:
            return int(box.id)
        except:
            return None
    return None


def color_for_id(tid):
    palette = [
        (102,126,234),
        (118,75,162),
        (16,185,129),
        (255,159,67),
        (255,99,71),
        (30,144,255)
    ]
    return palette[tid % len(palette)] if tid is not None else (0,255,0)
