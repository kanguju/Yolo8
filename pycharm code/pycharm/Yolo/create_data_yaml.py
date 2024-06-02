import os

# 베이스 디렉토리 경로 설정
base_dir = r'C:/Users/juwon/Desktop/machine learning/yolo'
unified_dataset = os.path.join(base_dir, 'unified_dataset')

# data.yaml 파일 작성
data_yaml_path = os.path.join(unified_dataset, 'data.yaml')

data_yaml_content = f"""
train: {os.path.join(unified_dataset, 'train/images').replace('\\', '/')}
val: {os.path.join(unified_dataset, 'valid/images').replace('\\', '/')}
test: {os.path.join(unified_dataset, 'test/images').replace('\\', '/')}

nc: 3  # 클래스 수
names: ['mask', 'glasses', 'cap']  # 클래스 이름
"""

with open(data_yaml_path, 'w') as file:
    file.write(data_yaml_content)

print(f'{data_yaml_path} 파일이 생성되었습니다.')
