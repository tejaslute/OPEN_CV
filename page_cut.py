import cv2
import numpy as np
print("package imported")
img=cv2.imread("Resources/SANKET.JPG")
print(img.shape)
#cv2.imshow("Output",img);
img_resize=cv2.resize(img,(600,600))
cv2.imshow("resize",img_resize)



width ,height =255,360
pts1=np.float32([[1529,2153],[3345,2153],[1489,5649],[2817,5033]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgoutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Output",imgoutput)

cv2.waitKey(0);