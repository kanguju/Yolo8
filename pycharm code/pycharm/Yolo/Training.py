from ultralytics import YOLO

# 모델 불러오기 (YOLOv8s 모델)
model = YOLO('yolov8s.pt')

# 모델 학습
model.train(data=r'C:\Users\juwon\Desktop\machine learning\yolo\unified_dataset\data.yaml', epochs=100, imgsz=640, batch=16)

# 학습 결과 확인
metrics = model.val()
print(metrics)

# 모델 저장
model.save('best.pt')
