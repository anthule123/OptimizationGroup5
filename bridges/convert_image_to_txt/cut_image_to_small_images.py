

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
        rowSize = self.image_np_array.shape[0]
        colSize = self.image_np_array.shape[1]
        row_step = self.image_np_array.shape[0]/self.row
        col_step = self.image_np_array.shape[1]/self.col 
        int_row_step = int(row_step)
        int_col_step = int(col_step)
        for i in range(self.row):
            for j in range(self.col):
                crop= crop_image(self.image_np_array, int(i/self.row*rowSize),
                                 int(j/self.col*colSize), 
                                 int_row_step, int_col_step)
                cv2.imwrite(f'{self.crop_folder_path}/crop_{i}_{j}.jpg', crop)
        
        