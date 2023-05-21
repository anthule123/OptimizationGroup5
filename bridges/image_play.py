import cv2
img=cv2.imread('digit.png',0) 
ret,thresh=cv2.threshold(img,127,255,0) 
edges=cv2.Canny(img,100,200) 
cv2.imshow('canny',edges)