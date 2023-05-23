

from PIL import Image, ImageFilter
import numpy as np
class DetectDigit:
    def __init__(self):
        self.prepare_data()
        
    def prepare_data(self):
        self.data = []
        self.labels = [i for i in range(9)]
        for i in range(9):
            img = Image.open(f'kmean/{i}.jpg').resize((28, 28))
            #làm mờ
            img = img.filter(ImageFilter.GaussianBlur(radius=1))
            img = img.convert('L')
            img = np.array(img)
            img = img.reshape(784)
            #chuẩn hóa
            img = img / 255
            self.data.append(img)
    
    def predict(self, img_path):
        img = Image.open(img_path).resize((28, 28))
        img =img.convert('L')
        img = np.array(img)
        img = img.reshape(784)
        img = img / 255
        #tính khoảng cách
        distances = [ np.linalg.norm(img - self.data[i]) for i in range(9)]
        #tìm khoảng cách nhỏ nhất
        min_index = np.argmin(distances)
        return self.labels[min_index]
    


