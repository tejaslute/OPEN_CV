import cv2
import numpy as np
print("package imported")

# image resize
'''
img=cv2.imread("Resources/photo.jpeg")
print(img.shape)
cv2.imshow("Output",img);
img_resize=cv2.resize(img,(600,600))
cv2.imshow("resize",img_resize);
cv2.waitKey(0);

'''

#cropped images

img=cv2.imread("Resources/photo.jpeg")
print(img.shape)
img_resize=cv2.resize(img,(600,600))
cv2.imshow("resize",img_resize);
igcropped=img[400:450,200:1000]
cv2.imshow("cropped",igcropped);
cv2.waitKey(0);


