import cv2
from ultralytics import YOLO

# 모델 파일 경로
model_path = r'C:\Users\juwon\PycharmProjects\Yolo\runs\detect\train7\weights\best.pt'

# 모델 로드
model = YOLO(model_path)

# 비디오 파일 경로
video_path = r'C:\Users\juwon\Desktop\machine learning\yolo\caps3.mp4'

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(video_path)

# 비디오 저장 설정
output_path = r'C:\Users\juwon\Desktop\machine learning\yolo\output_caps3.mp4'
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
    for result in results:
        annotated_frame = result.plot()

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
