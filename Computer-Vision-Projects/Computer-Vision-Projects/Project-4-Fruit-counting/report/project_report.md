# Fruit Counting and Yield Estimation — Project Report

## Abstract

This project demonstrates a computer vision pipeline for detecting
and counting visible fruits, measuring their image-space bounding
boxes, and calculating illustrative mass estimates.

## Problem Statement

Manual fruit counting is time-consuming. Image-based detection can
assist with counting and monitoring visible produce.

## Objectives

1. Detect supported fruit categories.
2. Count visible fruits.
3. Analyze bounding-box dimensions.
4. Demonstrate mass estimation using explicit assumptions.
5. Evaluate count accuracy against verified counts.

## Methodology

A pretrained YOLOv8n model detects supported fruit categories.
Detected instances are counted and their bounding-box dimensions
are recorded. Estimated mass is calculated using assumed average
masses per fruit category.

## Results

Generated outputs are stored in the results directory:
- fruit_detection_output.jpg
- fruit_counts.csv
- fruit_count_chart.png
- fruit_size_analysis.csv
- yield_estimation.csv
- yield_estimation_chart.png
- count_evaluation.csv

Insert actual results and a discussion after running the experiment.

## Performance Evaluation

Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) compare
predicted counts against manually verified counts.

## Limitations

The model may miss overlapping or unsupported fruits. Bounding boxes
do not directly measure physical dimensions. Estimated fruit mass
depends on assumed average weights and is not a validated orchard
yield prediction.

## Conclusion

The project demonstrates fruit detection and counting with basic
image-space analysis and illustrative mass estimation. A dedicated
fruit detector and a representative annotated dataset would be needed
for more robust agricultural applications.
