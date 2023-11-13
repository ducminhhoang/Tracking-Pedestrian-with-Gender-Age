# Age Gender Pedestrian With Tracking

A demo for train and test for your custom dataset on Yolov8 and EfficientNet-b3. Thanks for [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) and [EfficientNet-Pytorch](https://github.com/lukemelas/EfficientNet-PyTorch), I simply reuse these models to train and test appropriately for this problem.

## How I do
- Tracking Pedestrian with Yolov8
- Classification gender and age with EfficientNet-b3

<hr>

## Step 1: Prepare dataset
Format dataset following below:

```
- Dataset\
    - Tracking\
        - train\
            - images\
            - labels\
        - val\
            - images\
            - labels\
    - Age\
        - age_label.txt
        - baby\
        - young\
        ...
    - Gender\
        - gender_label.txt
        - male\
        - famale\
```

## Step 2: Train and export weights

## Step 3: Test