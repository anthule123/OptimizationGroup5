

import cv2


def crop_image(image, x, y, w, h):
    return image[x:x+w, y:y+h]


class CutImageToSmallImages:
    def __init__(self, image_np_array, row, col, crop_folder_path='crop'):
        self.image_np_array = image_np_array
        self.row = row
        self.col = col
        self.crop_folder_path = crop_folder_path
    def cut(self):
        row_step = self.image_np_array.shape[0]//self.row
        col_step = self.image_np_array.shape[1]//self.col 
        for i in range(self.row):
            for j in range(self.col):
                crop= crop_image(self.image_np_array, i*row_step, j*col_step, row_step, col_step)
                cv2.imwrite(f'{self.crop_folder_path}/crop_{i}_{j}.jpg', crop)
        
        