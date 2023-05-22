#lưu ý là mảng đầu vào phải là mảng 2 chiều, màu xám
class CropWhiteCorner:
    def __init__(self, image_np_array):
        self.image_np_array = image_np_array
        self.row = image_np_array.shape[0]
        self.col = image_np_array.shape[1]
    def sharpen(self):
        self.image_np_array[self.image_np_array<100] = 0
        self.image_np_array[self.image_np_array>=100] = 255
        
    def get_min_row(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.image_np_array[i][j] ==0:
                    return i
        
    def get_max_row(self):
        for i in range(self.row-1, -1, -1):
            for j in range(self.col):
                if self.image_np_array[i][j] == 0:
                    return i
    def get_min_col(self):
        for j in range(self.col):
            for i in range(self.row):
                if self.image_np_array[i][j] == 0:
                    return j
    def get_max_col(self):
        for j in range(self.col-1, -1, -1):
            for i in range(self.row):
                if self.image_np_array[i][j] == 0:
                    return j
    def nice_crop(self):
        self.sharpen()
        #print(self.image_np_array)
        min_row = self.get_min_row()
        max_row = self.get_max_row()
        min_col = self.get_min_col()
        max_col = self.get_max_col()
        if(min_row == None or max_row == None or min_col == None or max_col==None):
            return self.image_np_array
        width = max_col - min_col
        height = max_row - min_row
        new_min_row = max(0, int(min_row-height//3))
        new_max_row = min(max_row + height//3, self.row-1)
        new_min_col = max(0, int(min_col- height//3))
        new_max_col = min(max_col + width//3, self.col-1)
        return self.image_np_array[new_min_row:new_max_row+1, new_min_col:new_max_col+1]
    def crop(self):
        self.sharpen()
        #print(self.image_np_array)
        min_row = self.get_min_row()
        max_row = self.get_max_row()
        min_col = self.get_min_col()
        max_col = self.get_max_col()
        if(min_row == None or max_row == None or min_col == None or max_col==None):
            return self.image_np_array
        return self.image_np_array[min_row:max_row+1, min_col:max_col+1]