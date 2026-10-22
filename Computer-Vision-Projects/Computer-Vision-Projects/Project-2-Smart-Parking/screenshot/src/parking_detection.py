
import cv2
from ultralytics import YOLO


VEHICLE_CLASSES = {
    2: "Car",
    3: "Motorcycle",
    5: "Bus",
    7: "Truck"
}


def detect_vehicles(image_path, model_path="yolov8n.pt"):
    model = YOLO(model_path)

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    results = model.predict(
        source=image,
        imgsz=960,
        conf=0.15,
        classes=list(VEHICLE_CLASSES.keys()),
        verbose=False
    )

    detections = []

    for box in results[0].boxes:
        class_id = int(box.cls[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

        detections.append({
            "vehicle": VEHICLE_CLASSES[class_id],
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "confidence": float(box.conf[0])
        })

    return image, results[0].plot(), detections


def intersection_area(box_a, box_b):
    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b

    left = max(ax1, bx1)
    top = max(ay1, by1)
    right = min(ax2, bx2)
    bottom = min(ay2, by2)

    if right <= left or bottom <= top:
        return 0

    return (right - left) * (bottom - top)


def classify_parking_space(slot, detections, threshold=0.20):
    x1, y1, x2, y2 = slot
    area = max(1, (x2 - x1) * (y2 - y1))

    maximum_overlap = 0

    for detection in detections:
        vehicle_box = (
            detection["x1"],
            detection["y1"],
            detection["x2"],
            detection["y2"]
        )

        overlap = intersection_area(slot, vehicle_box) / area
        maximum_overlap = max(maximum_overlap, overlap)

    return maximum_overlap >= threshold, maximum_overlap
