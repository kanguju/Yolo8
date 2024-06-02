import os

# 라벨 파일 디렉토리 경로 설정
label_dirs = [
    r'C:\Users\juwon\Desktop\machine learning\yolo\unified_dataset\train\labels',
    r'C:\Users\juwon\Desktop\machine learning\yolo\unified_dataset\valid\labels',
    r'C:\Users\juwon\Desktop\machine learning\yolo\unified_dataset\test\labels'
]

# 클래스 이름 설정
class_names = ['mask', 'glasses', 'cap']

# 라벨 파일 확인 함수
def check_label_file(label_file_path):
    with open(label_file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 5:
                print(f"Incorrect format in {label_file_path}: {line}")
                return False
            class_index, x_center, y_center, width, height = parts
            class_index = int(class_index)
            x_center = float(x_center)
            y_center = float(y_center)
            width = float(width)
            height = float(height)
            if class_index < 0 or class_index >= len(class_names):
                print(f"Invalid class index in {label_file_path}: {class_index}")
                return False
            if not (0 <= x_center <= 1 and 0 <= y_center <= 1 and 0 <= width <= 1 and 0 <= height <= 1):
                print(f"Invalid bounding box values in {label_file_path}: {x_center}, {y_center}, {width}, {height}")
                return False
    return True

# 모든 라벨 파일 확인
all_files_valid = True
for label_dir in label_dirs:
    for label_file in os.listdir(label_dir):
        label_file_path = os.path.join(label_dir, label_file)
        if not check_label_file(label_file_path):
            all_files_valid = False

if all_files_valid:
    print("All label files are valid.")
else:
    print("Some label files are invalid.")
