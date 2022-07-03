import cv2
import numpy as np
print("package imported")

img=cv2.imread("Resources/photo.jpeg")
print(img.shape)
cv2.imshow("Output",img);
img_resize=cv2.resize(img,(600,600))
cv2.imshow("resize",img_resize);

image_horizantal=np.hstack((img_resize,img_resize))
cv2.imshow("Horixantal_imagesresize",image_horizantal);


image_verical=np.vstack((img_resize,img_resize))
cv2.imshow("vertical_images",image_verical);
cv2.waitKey(0);