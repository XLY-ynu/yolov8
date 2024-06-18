import os
import shutil
import random
import numpy as np
from sklearn.model_selection import train_test_split

random.seed(0)

val_size = 0.1
test_size = 0.2
postfix = 'jpg'
imgpath = 'JPEGImages'
txtpath = 'txt'  # 使用txt文件夹
# xmlpath = 'Annotations'  # 不再使用xml文件夹

os.makedirs('images/train', exist_ok=True)
os.makedirs('images/val', exist_ok=True)
os.makedirs('images/test', exist_ok=True)
os.makedirs('labels/train', exist_ok=True)
os.makedirs('labels/val', exist_ok=True)
os.makedirs('labels/test', exist_ok=True)

listdir = np.array([i for i in os.listdir(txtpath) if i.endswith('.txt')])  # 使用txt文件
random.shuffle(listdir)
train, val, test = listdir[:int(len(listdir) * (1 - val_size - test_size))], listdir[int(len(listdir) * (1 - val_size - test_size)):int(len(listdir) * (1 - test_size))], listdir[int(len(listdir) * (1 - test_size)):]
print(f'train set size:{len(train)} val set size:{len(val)} test set size:{len(test)}')

for i in train:
    shutil.copy(f'{imgpath}/{i[:-4]}.{postfix}', f'images/train/{i[:-4]}.{postfix}')
    shutil.copy(f'{txtpath}/{i}', f'labels/train/{i}')

for i in val:
    shutil.copy(f'{imgpath}/{i[:-4]}.{postfix}', f'images/val/{i[:-4]}.{postfix}')
    shutil.copy(f'{txtpath}/{i}', f'labels/val/{i}')

for i in test:
    shutil.copy(f'{imgpath}/{i[:-4]}.{postfix}', f'images/test/{i[:-4]}.{postfix}')
    shutil.copy(f'{txtpath}/{i}', f'labels/test/{i}')

print("文件划分完成。")
