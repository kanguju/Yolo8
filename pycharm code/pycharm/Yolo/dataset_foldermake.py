import os

base_dir = r'C:\Users\juwon\Desktop\기계학습\yolo'
unified_dataset = os.path.join(base_dir, 'unified_dataset')

# 통합 데이터셋 폴더 생성
os.makedirs(os.path.join(unified_dataset, 'train', 'images'), exist_ok=True)
os.makedirs(os.path.join(unified_dataset, 'train', 'labels'), exist_ok=True)
os.makedirs(os.path.join(unified_dataset, 'val', 'images'), exist_ok=True)
os.makedirs(os.path.join(unified_dataset, 'val', 'labels'), exist_ok=True)
os.makedirs(os.path.join(unified_dataset, 'test', 'images'), exist_ok=True)
os.makedirs(os.path.join(unified_dataset, 'test', 'labels'), exist_ok=True)
