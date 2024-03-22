import os

from skimage.io import imread
from skimage.transform import resize
import numpy as np

# prepare data
input_dir = r'C:\Users\tavin\OneDrive\Desktop\ai'
categories = ['Red-Triangles', 'Blue-Squares']

data = []
labels = []
for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img= resize(img, (15, 15))
        data.append(img.flatten())
        labels.append(category_idx)

data = np.asarray(data)
labels = np.asarray(labels)

