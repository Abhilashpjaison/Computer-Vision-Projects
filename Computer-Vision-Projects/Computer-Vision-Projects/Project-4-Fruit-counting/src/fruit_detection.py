
from ultralytics import YOLO
import cv2


FRUIT_CLASSES = {
    46: "Banana",
    47: "Apple",
    49: "Orange"
}


def detect_fruits(image_path, model_path="yolov8n.pt", confidence=0.20):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Unable to read image: {image_path}")

    model = YOLO(model_path)

    results = model.predict(
        source=image,
        conf=confidence,
        imgsz=960,
        classes=list(FRUIT_CLASSES.keys()),
        verbose=False
    )

    detections = []

    for box in results[0].boxes:
        class_id = int(box.cls[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

        detections.append({
            "fruit": FRUIT_CLASSES[class_id],
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "confidence": float(box.conf[0])
        })

    return image, results[0].plot(), detections
