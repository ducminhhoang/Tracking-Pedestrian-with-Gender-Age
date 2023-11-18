from ultralytics import YOLO

model = YOLO('yolov8m.pt')  # build a new model from YAML

# Train the model
results = model.train(data='person.yaml', epochs=1000, imgsz=640, lrf=0.001)
