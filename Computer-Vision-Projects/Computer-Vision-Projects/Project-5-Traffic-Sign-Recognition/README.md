# Traffic Sign Detection and Recognition Using Computer Vision

## 1. Problem Statement

Traffic signs provide important information about road rules, warnings,
and directions. Automated traffic-sign analysis is a useful computer
vision task for driver assistance and autonomous vehicles.

## 2. Objective

- Preprocess traffic-scene images.
- Identify candidate traffic-sign regions.
- Visualize detected candidates.
- Compare candidate boxes against manually annotated ground truth.
- Document the distinction between detection and recognition.

## 3. Dataset

This demonstration uses a user-provided traffic-scene image.
No separate dataset is downloaded.

See `dataset/README.md`.

## 4. Methodology

1. Load the traffic-scene image.
2. Resize large images.
3. Convert the image to HSV.
4. Segment red and blue regions.
5. Apply morphological operations.
6. Extract contours and filter candidate regions.
7. Visualize bounding boxes.
8. Evaluate candidate detection using IoU-based matching.

## 5. Tools and Libraries

- Python
- Google Colab
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## 6. Results

The system generates candidate detection images, segmentation masks,
CSV summaries, and detection evaluation metrics.

## 7. Performance Evaluation

Precision, recall, and F1-score are calculated using manually verified
bounding boxes and an IoU threshold of 0.50.

These metrics evaluate candidate-region detection, not semantic
traffic-sign recognition.

## 8. Limitations

- Color segmentation can detect unrelated red and blue objects.
- Lighting and shadows affect detection.
- Small and occluded signs may be missed.
- The baseline does not identify the meaning of traffic signs.
- A single image is not sufficient to establish general performance.

## 9. Conclusion

This project demonstrates a classical computer vision baseline for
traffic-sign candidate detection. Reliable recognition requires a
trained classifier or detector with verified class labels.

## 10. How to Run

Open `Traffic_Sign_Detection_Recognition.ipynb` in Google Colab and
run the cells in order. Upload a road image and provide verified
ground-truth annotations before interpreting evaluation metrics.
