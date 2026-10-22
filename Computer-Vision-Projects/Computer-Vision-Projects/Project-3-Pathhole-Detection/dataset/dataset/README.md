# Dataset Information

## Dataset approach

This project uses a user-provided parking-lot image rather than
a separately downloaded parking dataset.

## Input

The input is a parking-lot image containing vehicles and parking
spaces.

## Annotation

Parking-space regions are manually defined using image coordinates.
Ground-truth occupancy labels must be manually verified.

## Important limitation

A single input image is suitable for demonstrating the pipeline,
but it is not sufficient to establish general parking-occupancy
performance.

For a more rigorous evaluation, test on multiple independent images
with verified occupied and available parking-space labels.

## Pretrained model

Vehicle detection uses the pretrained YOLOv8n model. Its weights
are obtained through the Ultralytics model-loading process.

The pretrained model is not a parking-space dataset.
