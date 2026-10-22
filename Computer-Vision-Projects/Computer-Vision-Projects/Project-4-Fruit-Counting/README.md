# Fruit Counting and Yield Estimation Using Computer Vision

## Problem statement
Develop a computer-vision solution for the task described by this project title.

## Objective
- Implement a reproducible pipeline for the selected task.
- Preprocess and inspect the dataset.
- Generate visual outputs for inspection.
- Evaluate predictions against ground-truth annotations.
- Document limitations and future improvements.

## Dataset
- **Dataset:** Select and document a fruit image dataset appropriate to the target crop
- **Source:** https://www.kaggle.com/datasets
- **Labels:** verify annotation format and image/label matching before evaluation.
- **License:** check the source's terms before using or redistributing data.

See [DATASET.md](DATASET.md).

## Methodology
1. Load and inspect the images and annotations.
2. Preprocess images as appropriate for the task.
3. Apply a task-specific classical CV method or trained model.
4. Save predictions and input/output visualizations.
5. Compare predictions with ground truth using suitable metrics.

## Tools/libraries used
- `opencv-python`
- `numpy`
- `matplotlib`
- `pandas`
- `scikit-learn`

## Results
This starter repository has no measured results yet. Add results only after running the implementation.

## Performance evaluation
Select suitable metrics for the task, such as precision, recall, F1-score, IoU, accuracy, mAP, or count error. Document the test split and report only values actually computed from ground-truth labels.

## Screenshots/visualizations
Save representative input/output comparisons in `screenshots/`.

## Limitations
Record the actual failure cases observed during testing, such as lighting, occlusion, class imbalance, or annotation limitations.

## Conclusion
Complete after experiments. Summarize the implemented method, measured results, observed limitations, and next improvements.
