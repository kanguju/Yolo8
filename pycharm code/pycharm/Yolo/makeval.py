import os
import shutil
from glob import glob
import random

##마스크에 valid 파일이없어 taining 파일에서 일부데이터를 떄어서 만들었습니다.



def move_files(src_images, src_labels, dest_images, dest_labels, fraction=0.2):
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

    num_files_to_move = int(len(image_files) * fraction)
    selected_images = random.sample(image_files, num_files_to_move)

    for img_file in selected_images:
        label_file = img_file.replace('images', 'labels').replace('.jpg', '.txt')
        if os.path.exists(label_file):
            shutil.move(img_file, dest_images)
            shutil.move(label_file, dest_labels)
            print(f"Moved {img_file} and {label_file} to {dest_images} and {dest_labels}")
        else:
            print(f"Label file {label_file} not found, skipping {img_file}")

# 베이스 디렉토리 경로 설정
base_dir = r'C:\Users\juwon\Desktop\기계학습\yolo\mask-detaction.v1i.yolov8'  # 경로 수정

# 검증 데이터셋 폴더 생성
val_images_dest = os.path.join(base_dir, 'val', 'images')
val_labels_dest = os.path.join(base_dir, 'val', 'labels')

os.makedirs(val_images_dest, exist_ok=True)
os.makedirs(val_labels_dest, exist_ok=True)

# 학습 데이터셋 폴더 설정
train_images_src = os.path.join(base_dir, 'train', 'images')
train_labels_src = os.path.join(base_dir, 'train', 'labels')

# 학습 데이터셋의 일부를 검증 데이터셋으로 이동
move_files(train_images_src, train_labels_src, val_images_dest, val_labels_dest, fraction=0.2)

print('검증 데이터셋 생성 완료')
