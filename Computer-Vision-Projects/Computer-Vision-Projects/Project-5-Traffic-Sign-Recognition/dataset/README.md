# Dataset Information

## Data Source

This project uses a user-provided road image. No separate dataset
is downloaded.

## Input

The image should contain visible traffic signs.

## Annotation

Ground-truth signs should be represented by bounding boxes and
verified semantic labels.

## Detection Method

Candidate signs are identified using HSV color segmentation,
morphological processing, contour extraction, and geometric filtering.

## Limitations

Color segmentation is sensitive to lighting and background objects.
It does not provide reliable semantic traffic-sign recognition.

For robust recognition, a trained traffic-sign classifier or detector
and a representative labeled evaluation set are required.
