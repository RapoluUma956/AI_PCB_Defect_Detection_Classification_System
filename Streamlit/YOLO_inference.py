import os
import time
import numpy as np
import torch
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw, ImageFont
from ultralytics import YOLO


#==================================================
#LOAD YOLO MODEL
#==================================================

print("--- PCB YOLOv8 Detection Pipeline ---")

MODEL_PATH = "Model/best_yolov8_pcb_defects.pt"

print("🔍 Loading YOLO model...")
yolo_model = YOLO(MODEL_PATH)

class_names = yolo_model.names
print(f"✅ Classes loaded: {class_names}")

#YOLO DETECTION FUNCTION

def detect_with_yolo(input_image):
    print("🔍 Running YOLO inference...")

    results = yolo_model.predict(
        source=input_image,
        conf=0.35,
        iou=0.5,
        device="cpu",   # change to 0 if CUDA exists
        verbose=False
    )

    detections = []

    for r in results:
        if r.boxes is None:
            continue

        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])

            detections.append({
                "box": [int(x1), int(y1), int(x2), int(y2)],
                "label": class_names[cls_id],
                "confidence": confidence
            })

    print(f"✅ YOLO detected {len(detections)} defects")
    return detections

#DRAW FUNCTION
def expand_box(box, img_w, img_h, scale=1.3):
    """
    box: [x1, y1, x2, y2]
    scale: >1 enlarges box
    """
    x1, y1, x2, y2 = box
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    w = (x2 - x1) * scale
    h = (y2 - y1) * scale

    nx1 = max(0, cx - w / 2)
    ny1 = max(0, cy - h / 2)
    nx2 = min(img_w, cx + w / 2)
    ny2 = min(img_h, cy + h / 2)

    return [int(nx1), int(ny1), int(nx2), int(ny2)]


def draw_detections_on_image(image, detections):
    img_with_boxes = image.copy()
    draw = ImageDraw.Draw(img_with_boxes)

    img_w, img_h = image.size

    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 32)
    except:
        font = ImageFont.load_default()

    for det in detections:

        box = det["box"]  # [x1, y1, x2, y2]

        box = expand_box(box, img_w, img_h, scale=1.4)

        label = det["label"]
        confidence = det["confidence"]

        draw.rectangle(box, outline=(255, 0, 0), width=4)

        text = f"{label} ({confidence:.2f})"
        text_bbox = draw.textbbox((0, 0), text, font=font)
        tw = text_bbox[2] - text_bbox[0]
        th = text_bbox[3] - text_bbox[1]

        draw.rectangle(
            [box[0], box[1] - th - 6, box[0] + tw + 8, box[1]],
            fill="white"
        )
        draw.text(
            (box[0] + 4, box[1] - th - 4),
            text,
            fill="red",
            font=font
        )

    return img_with_boxes


#STREAMLIT BACKEND FUNCTION

def run_inference_on_pil(input_image):
    """Exact same Streamlit backend interface"""

    start_time = time.time()
    print("🔍 Starting PCB defect detection using YOLO...")

    anomalies = detect_with_yolo(input_image)

    result_image = draw_detections_on_image(input_image, anomalies)

    elapsed = time.time() - start_time
    print(f"✅ Detection complete: {len(anomalies)} defects in {elapsed:.2f}s")
    print(f"   Classes used: {list(class_names.values())}")

    return result_image, anomalies

#TEST RUN

print("✅ PIPELINE READY (YOLO BACKEND)")
print("Run: streamlit run app.py")
