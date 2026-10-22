
import cv2
import numpy as np
import math


def preprocess_image(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    return gray, blurred


def detect_edges(image):

    gray, blurred = preprocess_image(image)

    return cv2.Canny(
        blurred,
        50,
        150
    )


def region_of_interest(edges):

    height, width = edges.shape

    mask = np.zeros_like(edges)

    polygon = np.array([[
        (0, height),
        (width, height),
        (int(width * 0.75), int(height * 0.55)),
        (int(width * 0.25), int(height * 0.55))
    ]], dtype=np.int32)

    cv2.fillPoly(
        mask,
        polygon,
        255
    )

    return cv2.bitwise_and(
        edges,
        mask
    )


def detect_hough_lines(edges):

    return cv2.HoughLinesP(
        edges,
        1,
        np.pi / 180,
        threshold=20,
        minLineLength=20,
        maxLineGap=30
    )
