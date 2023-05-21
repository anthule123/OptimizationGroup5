# bridges

B1: Viết 1 bài toán dạng đơn giản như ở https://github.com/anthule123/bridges/blob/main/bridge_game.txt:

.4..3.3.3

..1..2.1.

.2.......

2..2.2..4

.........

3..3.1..2

.......2.

.1.3..2..

2.2.3..3.
     
   Xử lí: 
          
          1.1. Xây dựng mô hình bài toán
          1.2. Xây dựng mô hình giải 
           
Tạm xong với trường hợp small 9x9 như ở input_reader.ipynb

B2: muốn đưa trường hợp lớn hơn, như là 14x22 hoặc 25x25. Thử sử dụng công cụ xử lí ảnh
       -  
       
           1.1. Import bức ảnh, chuyển sang numpy array và grayscale
           1.2. Cắt bỏ phần viền trắng
           1.3. Chia thành nxm bức ảnh con (nxm là kích thước của bức ảnh)
           1.4. Resize mỗi bức ảnh con thành 28x28 
           1.5. Mỗi bức ảnh sẽ trông như 
           
   ![crop_4_20](https://github.com/anthule123/bridges/assets/29473579/09266e13-b42a-4988-901c-ff44444d69b9)
                    hoặc ![crop_5_3](https://github.com/anthule123/bridges/assets/29473579/4b1a9a99-6795-46bf-a35a-07d039d0f86d)
                Ta phải xử lí xóa phần viền hình tròn đi thì mới sử dụng keras để nhận dạng chữ viết tay được
                
           1.6 Ta đưa mỗi bức ảnh -> về con số tương ứng hoặc dấu . nếu ko có số nào
      
   -Rồi quay lại dùng B1 để giải bài toán
     
B3: In ra bức ảnh solution

       Dùng p5.js hoặc pygame
