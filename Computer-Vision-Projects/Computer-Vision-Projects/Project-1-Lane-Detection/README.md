
# Road Lane Detection and Departure Warning

## 1. Problem Statement

Lane departure is a major road safety concern. A computer vision
system can detect road lane boundaries and estimate whether a vehicle
is moving away from the center of its lane.

## 2. Objective

The objective of this project is to develop a classical computer
vision based system capable of:

- Detecting lane boundaries
- Estimating the lane center
- Estimating vehicle/image center
- Calculating lateral deviation
- Generating lane departure warnings

## 3. Dataset

KITTI Road/Lane Detection Dataset 224 x 224.

Dataset source:
https://www.kaggle.com/datasets/kpgeek/kitti-roadlane-detection-dataset-224-x-224

## 4. Methodology

Input Image
→ Grayscale Conversion
→ Gaussian Blur
→ Canny Edge Detection
→ Region of Interest
→ Hough Transform
→ Lane Boundary Detection
→ Lane Center Estimation
→ Lateral Deviation
→ Departure Warning

## 5. Technologies

- Python
- OpenCV
- NumPy
- Matplotlib
- Pandas
- Scikit-learn
- Google Colab

## 6. Performance Evaluation

The system can be evaluated using:

- Precision
- Recall
- F1-score
- Intersection over Union (IoU)

Ground-truth annotations are used for quantitative evaluation.

## 7. Limitations

- Performance can decrease under poor lighting.
- Shadows can affect lane detection.
- Strongly curved lanes may not be represented accurately by straight
  line models.
- Occluded lane markings can reduce detection performance.
- Road markings with unusual colors may be difficult to detect.
- The system uses classical computer vision rather than a trained
  deep learning model.

## 8. Conclusion

A classical computer vision pipeline was developed for road lane
detection and lane departure warning. The system combines edge
detection, region-of-interest processing and Hough line detection to
estimate lane boundaries and determine lateral deviation.
