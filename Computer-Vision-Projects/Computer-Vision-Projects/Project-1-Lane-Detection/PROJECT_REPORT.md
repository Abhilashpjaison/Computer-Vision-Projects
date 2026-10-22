
# Project Report

## Title

Road Lane Detection and Departure Warning Using Computer Vision

## 1. Introduction

Lane detection is an important computer vision application for
advanced driver assistance systems and autonomous vehicles.

The purpose of this project is to identify lane boundaries from road
images and determine whether the vehicle is deviating from the lane.

## 2. Problem Statement

A vehicle moving away from its lane center may cause a collision.
Therefore, an automated system that detects lane boundaries and warns
the driver about lane departure can improve road safety.

## 3. Objective

The objectives are:

1. Detect lane boundaries.
2. Estimate the lane center.
3. Calculate lateral deviation.
4. Generate a lane departure warning.
5. Evaluate the detection performance.

## 4. Methodology

The following classical computer vision pipeline is used:

Input Image
→ Grayscale
→ Gaussian Blur
→ Canny Edge Detection
→ Region of Interest
→ Hough Transform
→ Lane Boundary Detection
→ Lane Center
→ Lateral Deviation
→ Departure Warning

## 5. Results

Sample results are stored in the results and screenshots folders.

Quantitative performance metrics should be calculated using the
dataset ground-truth annotations.

## 6. Limitations

The method may be affected by shadows, poor illumination, occlusion,
worn lane markings and highly curved roads.

## 7. Future Improvements

Future versions can use:

- Perspective transformation
- Polynomial lane fitting
- Camera calibration
- Deep learning based lane segmentation
- Real-time video processing
- Vehicle speed estimation
- Steering correction

## 8. Conclusion

The project demonstrates how classical computer vision techniques
can be combined to detect road lanes and generate lane departure
warnings.
