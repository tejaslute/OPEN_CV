import cv2
import numpy as np
print("package imported")

img=np.ones((512,512,3),np.uint8)
print(img.shape)
cv2.line(img,(0,0),(400,400),(0,255,0),3)
cv2.imshow("resize_line",img);

cv2.rectangle(img,(0,0),(400,400),(0,14,0),5)
cv2.imshow("rectangle ",img);
cv2.rectangle(img,(0,0),(400,400),(0,14,0),cv2.FILLED)
cv2.imshow("rectangle_filled ",img);

cv2.putText(img,"OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(1,150,1),1)
cv2.imshow("Text_filled ",img);
cv2.waitKey(0);