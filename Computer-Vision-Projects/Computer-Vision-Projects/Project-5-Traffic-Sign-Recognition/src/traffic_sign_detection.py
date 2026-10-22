
import cv2
import numpy as np


def detect_traffic_sign_candidates(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Unable to read image: {image_path}")

    height, width = image.shape[:2]
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    red1 = cv2.inRange(
        hsv,
        np.array([0, 70, 50]),
        np.array([10, 255, 255])
    )

    red2 = cv2.inRange(
        hsv,
        np.array([170, 70, 50]),
        np.array([180, 255, 255])
    )

    blue = cv2.inRange(
        hsv,
        np.array([90, 60, 40]),
        np.array([135, 255, 255])
    )

    mask = cv2.bitwise_or(
        cv2.bitwise_or(red1, red2),
        blue
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (5, 5)
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    candidates = []

    min_area = max(100, int(height * width * 0.0001))
    max_area = int(height * width * 0.15)

    for contour in contours:
        area = cv2.contourArea(contour)

        if not min_area <= area <= max_area:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        if w < 12 or h < 12:
            continue

        ratio = w / max(h, 1)

        if 0.45 <= ratio <= 1.8:
            candidates.append({
                "x1": x,
                "y1": y,
                "x2": x + w,
                "y2": y + h,
                "area": float(area)
            })

    output = image.copy()

    for item in candidates:
        cv2.rectangle(
            output,
            (item["x1"], item["y1"]),
            (item["x2"], item["y2"]),
            (0, 255, 0),
            2
        )

    return image, mask, output, candidates
