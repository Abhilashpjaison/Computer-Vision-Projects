# Traffic Sign Detection and Recognition — Project Report

## Abstract

This project demonstrates a classical image-processing approach for
identifying candidate traffic-sign regions in road images.

## Problem Statement

Traffic signs communicate road rules and warnings. Automated
detection can support intelligent transportation systems.

## Objectives

1. Preprocess traffic-scene images.
2. Identify candidate sign regions.
3. Visualize candidate bounding boxes.
4. Evaluate detection against manually annotated signs.

## Methodology

The input image is converted to HSV color space. Red and blue masks
are generated and cleaned using morphological operations. Contours
are extracted and filtered using area and aspect ratio.

## Results

Generated files are stored in the results directory:
- traffic_sign_candidates.jpg
- traffic_sign_mask.png
- preprocessed_image.jpg
- traffic_sign_candidates.csv
- detection_summary.csv
- evaluation.csv

Discuss actual outputs after running the notebook.

## Performance Evaluation

Precision, recall, and F1-score are calculated using one-to-one
matching between predicted candidate boxes and ground-truth boxes
at an IoU threshold of 0.50.

## Limitations

The baseline identifies color-based candidate regions, not reliable
semantic sign categories. Similar-colored objects may be detected,
and signs with unusual colors or poor visibility may be missed.

## Conclusion

The project provides a classical computer vision baseline for
traffic-sign candidate detection. A dedicated trained traffic-sign
recognition model would be needed to identify specific sign meanings
reliably.
