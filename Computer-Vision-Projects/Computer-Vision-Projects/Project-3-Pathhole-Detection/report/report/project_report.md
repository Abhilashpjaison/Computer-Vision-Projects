# Pothole Detection — Project Report

## Abstract

This project implements a classical computer vision pipeline for
identifying candidate pothole regions in road images.

## Problem Statement

Potholes are road-surface defects that can affect road safety and
vehicle performance. Image processing can assist in identifying
regions that require further inspection.

## Objectives

1. Preprocess road images.
2. Identify candidate regions.
3. Generate bounding-box visualizations.
4. Evaluate predictions using annotated ground truth.

## Methodology

The input image is converted to grayscale, smoothed using Gaussian
blur, and enhanced using CLAHE. Adaptive thresholding and morphological
operations produce a candidate mask. Contour analysis extracts
regions that satisfy size constraints.

## Results

Generated files are stored in the results directory:
- pothole_detection_output.jpg
- preprocessed_image.jpg
- candidate_mask.png
- detected_candidates.csv
- detection_summary.csv
- evaluation.csv

Actual results and verified evaluation scores should be discussed
after running the experiment.

## Performance Evaluation

Predicted bounding boxes are matched to manually annotated potholes
using an IoU threshold of 0.50. Precision, recall, and F1-score
are calculated from the resulting true positives, false positives,
and false negatives.

## Limitations

Shadows, road markings, cracks, and repairs can produce false
detections. Some potholes may be missed. Performance may vary with
lighting, image resolution, and road-surface appearance.

## Conclusion

The project provides a baseline pothole-candidate detection system.
A specialized trained model and a larger annotated test set would
be appropriate next steps for more reliable detection.
