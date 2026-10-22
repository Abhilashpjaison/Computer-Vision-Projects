# Dataset Information

## Data source

This demonstration uses user-provided road images. No separate
dataset is downloaded.

## Image contents

The input image should show a road surface, ideally containing
one or more visible potholes.

## Annotation format

Ground-truth potholes are represented as bounding boxes:

[x1, y1, x2, y2]

Coordinates are measured in pixels.

## Evaluation

Predictions are compared with manually verified annotations using
an IoU threshold of 0.50.

## Limitations

A single image is not sufficient to demonstrate generalization.
Road shadows, cracks, repairs, stains, and surface texture can
produce false detections.

For rigorous evaluation, use multiple independently annotated
images and report aggregate performance.
