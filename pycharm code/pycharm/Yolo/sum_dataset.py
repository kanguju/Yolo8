import os
import shutil
from glob import glob

def move_files(src_images, src_labels, dest_images, dest_labels):
    if not os.path.exists(src_images):
        print(f"Source images directory {src_images} does not exist!")
        return
    if not os.path.exists(src_labels):
        print(f"Source labels directory {src_labels} does not exist!")
        return

    image_files = glob(os.path.join(src_images, '*.jpg'))
    label_files = glob(os.path.join(src_labels, '*.txt'))

    if not image_files:
        print(f"No image files found in {src_images}")
        return
    if not label_files:
        print(f"No label files found in {src_labels}")
        return

    for img_file in image_files:
        label_file = img_file.replace('images', 'labels').replace('.jpg', '.txt')
        if os.path.exists(label_file):
            shutil.copy(img_file, dest_images)
            shutil.copy(label_file, dest_labels)
            print(f"Copied {img_file} and {label_file} to {dest_images} and {dest_labels}")
        else:
            print(f"Label file {label_file} not found, skipping {img_file}")

# 베이스 디렉토리 경로 설정
base_dir = r'C:/Users/juwon/Desktop/machine learning/yolo'
unified_dataset = os.path.join(base_dir, 'unified_dataset')

# 검증 데이터셋 폴더 생성
valid_images_dest = os.path.join(unified_dataset, 'valid', 'images')
valid_labels_dest = os.path.join(unified_dataset, 'valid', 'labels')

os.makedirs(valid_images_dest, exist_ok=True)
os.makedirs(valid_labels_dest, exist_ok=True)

# 데이터셋 경로 설정
datasets = [
    os.path.join(base_dir, 'mask-detection.v1i.yolov8', 'valid'),
    os.path.join(base_dir, 'PEX5.v4i.yolov8', 'valid'),
    os.path.join(base_dir, 'Usman.v1i.yolov8', 'valid')
]

# 데이터셋 통합
for dataset in datasets:
    valid_images_src = os.path.join(dataset, 'images')
    valid_labels_src = os.path.join(dataset, 'labels')
    move_files(valid_images_src, valid_labels_src, valid_images_dest, valid_labels_dest)

print('검증 데이터셋 통합 완료')
