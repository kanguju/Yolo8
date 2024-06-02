import os

# 라벨 파일 디렉토리 경로 설정
label_dirs = [
    r'C:\Users\juwon\Desktop\machine learning\yolo\unified_dataset\train\labels',
    r'C:\Users\juwon\Desktop\machine learning\yolo\unified_dataset\valid\labels',
    r'C:\Users\juwon\Desktop\machine learning\yolo\unified_dataset\test\labels'
]

# 라벨 파일 확인 및 수정 함수
def fix_label_file(label_file_path):
    with open(label_file_path, 'r') as file:
        lines = file.readlines()

    corrected_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 5:
            print(f"Incorrect format in {label_file_path}: {line}")
            continue  # 이 줄을 건너뛰고 계속 진행

        class_index, x_center, y_center, width, height = parts
        corrected_line = f"{class_index} {x_center} {y_center} {width} {height}\n"
        corrected_lines.append(corrected_line)

    if corrected_lines:
        with open(label_file_path, 'w') as file:
            file.writelines(corrected_lines)
        print(f"Fixed {label_file_path}")

# 모든 라벨 파일 확인 및 수정
for label_dir in label_dirs:
    for label_file in os.listdir(label_dir):
        label_file_path = os.path.join(label_dir, label_file)
        fix_label_file(label_file_path)

# 모델 재학습 및 검증 코드
from ultralytics import YOLO

# 모델 파일 경로
model_path = r'C:\Users\juwon\PycharmProjects\Yolo\runs\detect\train7\weights\best.pt'

# 모델 로드
model = YOLO(model_path)

# 학습 데이터 경로 설정
data_yaml_path = r'C:\Users\juwon\Desktop\machine learning\yolo\unified_dataset\data.yaml'

# 모델 재학습
model.train(data=data_yaml_path, epochs=10, imgsz=640, batch=16)

# 학습 결과 확인
metrics = model.val()
print(metrics)

# 모델 저장
model.save('best_retrained.pt')

# 비디오 처리 및 저장 코드
import cv2

# 비디오 파일 경로
video_path = r'C:\Users\juwon\Desktop\machine learning\yolo\caps.mp4'

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(video_path)

# 비디오 저장 설정
output_path = r'C:\Users\juwon\Desktop\machine learning\yolo\output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

frame_count = 0
max_frames = fps * 5  # 5초 비디오

while cap.isOpened() and frame_count < max_frames:
    ret, frame = cap.read()
    if not ret:
        break

    # 객체 검출 수행
    results = model(frame)

    # 결과를 비디오 프레임에 반영
    annotated_frame = results[0].plot()

    # 비디오 파일에 프레임 저장
    out.write(annotated_frame)

    # 결과 시각화 (원한다면)
    cv2.imshow('Frame', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_count += 1

# 비디오 캡처 객체 및 비디오 파일 객체 해제
cap.release()
out.release()
cv2.destroyAllWindows()

print(f'5초짜리 비디오가 {output_path}에 저장되었습니다.')
