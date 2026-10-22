
import cv2


def detect_pothole_candidates(image_path, min_area=150, max_area_ratio=0.30):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Unable to read image: {image_path}")

    height, width = image.shape[:2]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(blurred)

    mask = cv2.adaptiveThreshold(
        enhanced,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        31,
        8
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

    max_area = int(height * width * max_area_ratio)

    for contour in contours:
        area = cv2.contourArea(contour)

        if area < min_area or area > max_area:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        if w < 10 or h < 10:
            continue

        candidates.append({
            "x1": x,
            "y1": y,
            "x2": x + w,
            "y2": y + h,
            "area": float(area)
        })

    output = image.copy()

    for candidate in candidates:
        cv2.rectangle(
            output,
            (candidate["x1"], candidate["y1"]),
            (candidate["x2"], candidate["y2"]),
            (0, 0, 255),
            2
        )

    return image, mask, output, candidates
