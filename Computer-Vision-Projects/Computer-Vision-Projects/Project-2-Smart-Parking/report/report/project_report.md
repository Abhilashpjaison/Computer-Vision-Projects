# Smart Parking Space Detection — Project Report

## Abstract

This project demonstrates a computer vision pipeline for detecting
vehicles in a parking-lot image and estimating the occupancy of
manually defined parking spaces.

## Problem Statement

Manually identifying available parking spaces is inconvenient.
An image-based system can help estimate which spaces are occupied.

## Objectives

1. Detect vehicles in a parking image.
2. Estimate occupancy for defined parking regions.
3. Visualize the output.
4. Evaluate predictions against verified occupancy labels.

## Methodology

The system loads an input image and applies a pretrained YOLOv8n
model to detect vehicles. Rectangular regions are defined for
individual parking spaces. Vehicle-box overlap is used as a baseline
heuristic to estimate occupancy.

## Results

Refer to the generated files in the `results/` folder:
- parking_occupancy_output.jpg
- vehicle_detection_output.jpg
- parking_status.csv
- evaluation.csv
- confusion_matrix.png
- occupancy_summary.png

Insert a discussion of the actual outputs and verified metrics
after running the experiment.

## Limitations

Parking regions require manual definition. Vehicle detection can
miss objects or generate incorrect bounding boxes. The overlap
heuristic can incorrectly assign vehicles to parking spaces.
A single image is not sufficient to demonstrate performance
across different parking conditions.

## Conclusion

The project provides a baseline demonstration of vehicle detection
and occupancy estimation. A larger labeled dataset and more
robust parking-space localization would be needed for a reliable
real-world parking management system.
