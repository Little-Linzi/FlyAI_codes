import os

from torch.utils.data import Dataset
import torch
from PIL import Image
import numpy as np
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

DATA_PATH = 'data/input/MushroomsRecognition/'
class MyDataset(Dataset):
    def __init__(self, input_x, input_y, transform=None):
        self.file_names = input_x
        self.label = input_y
        self.transform = transform

    def __len__(self):
        return len(self.label)

    def __getitem__(self, idx):
        path = os.path.join(DATA_PATH, self.file_names[idx])
        image = Image.open(path).convert("RGB")
        if self.transform is not None:
            image = self.transform(image)
        label = self.label[idx]

        return image, int(label)