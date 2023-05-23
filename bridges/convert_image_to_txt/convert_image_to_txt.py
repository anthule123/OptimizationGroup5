from PIL import Image
import cv2
import numpy as np
from clear_bad_boundary import ClearBadBoundary
from detect_digit import DetectDigit
from recognize_digit import RecognizeDigit
from cut_image_to_small_images import CutImageToSmallImages
from crop_white_corner import CropWhiteCorner
class ConvertImageToTxt:
    def __init__(self, image_path, txt_path, row, col):
        self.image_path = image_path
        self.txt_path = txt_path
        self.row = row
        self.col = col 
        self.data_array = np.zeros((self.row, self.col))
    
    def convert_to_numpy_array(self):
        self.raw_image = Image.open(self.image_path)
        self.gray_image = self.raw_image.convert('L')
        self.gray_np = np.array(self.gray_image)
    
    def crop_white_corner(self):
        cropper = CropWhiteCorner(self.gray_np)
        self.gray_np = cropper.crop()
    def cut(self):
        cutter = CutImageToSmallImages(self.gray_np, self.row, self.col)
        cutter.cut()
    def clear(self):
        for i in range(self.row):
            for j in range(self.col):
                clear = ClearBadBoundary(f'crop/crop_{i}_{j}.jpg')
                clear.clear()
                #crop white corner của cái crop/
                img = Image.open(f'crop/crop_{i}_{j}.jpg_clear.jpg').convert('L')
                img_np = np.array(img)
                cropper = CropWhiteCorner(img_np)
                after_crop = cropper.crop()
                #lưu ảnh
                cv2.imwrite(f'crop/crop_{i}_{j}.jpg_clear.jpg', after_crop)
                
    def make_data_array(self):
        detector = DetectDigit()
        #Tạo string gồm row dòng, mỗi dòng có col kí tự
        read_txt= ""
        for i in range(self.row):
            for j in range(self.col):
                self.data_array[i][j] = detector.predict(f'crop/crop_{i}_{j}.jpg_clear.jpg')
                if(self.data_array[i][j] == 0):
                    read_txt += "."
                else:
                    read_txt += str(int(self.data_array[i][j]))
            read_txt += "\n"
        #Lưu string vào file txt
        with open(self.txt_path, 'w') as f:
            f.write(read_txt)
    def convert(self):
        self.convert_to_numpy_array()
        self.crop_white_corner()
        self.cut()
        self.clear()
        self.make_data_array()