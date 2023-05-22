from PIL import Image
import cv2
import numpy as np
class ClearBadBoundary:
    def __init__(self, image_path):
        self.image_path = image_path
        image_raw = Image.open(image_path)
        image_raw = image_raw.convert('L')
        self.image_np_array = np.array(image_raw)
        self.visited = set()
        self.gray = set()
        self.dominant_color = 255 
        self.row = self.image_np_array.shape[0]
        self.col = self.image_np_array.shape[1]
    def sharpen(self):
        self.image_np_array[self.image_np_array < 100] = 0
        self.image_np_array[self.image_np_array >= 100] = 255
    def get_boundary(self):
        self.boundaries = set()
        for i in range(0, self.row):
            self.boundaries.add((i, 0))
            self.boundaries.add((i, self.col-1))
        for j in range(0, self.col):
            self.boundaries.add((0, j))
            self.boundaries.add((self.row-1, j))
    def find_dominant_color(self):
        count_black = 0
        count_white = 0
        for (i, j) in self.boundaries:
                if self.image_np_array[i][j]<=100:
                    count_black += 1
                else:
                    count_white += 1
        if count_black > count_white:
            self.dominant_color = 0
        else:
            self.dominant_color = 255
    def dfs(self, x, y):
        #print(self.image_np_array[x][y])
        if(self.image_np_array[x][y] == self.dominant_color):
            return None
        self.gray.add((x, y))
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i!=0 or j!=0:
                    if x+i >= 0 and x+i < self.row and y+j >= 0 and y+j < self.col:
                        if ((x+i, y+j) not in self.visited and
                            (x+i, y+j) not in self.gray):
                                self.dfs(x+i, y+j)
        self.visited.add((x, y))
        self.image_np_array[x,y] = self.dominant_color
    def clear(self):
        self.sharpen()
        self.get_boundary()
        self.find_dominant_color()
        self.visited = set()
        self.gray = set()
        for pixel in self.boundaries:
            self.dfs(pixel[0], pixel[1])
        #lưu lại ảnh đã xử lý
        cv2.imwrite(f'{self.image_path}_clear.jpg', self.image_np_array)
        return None