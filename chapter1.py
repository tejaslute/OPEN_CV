import cv2
import numpy as np
print("package imported")

# image
'''
img=cv2.imread("Resources/photo.jpeg")
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Output",img);
cv2.waitKey(0);
'''

# vedio

'''cap=cv2.VideoCapture("Resources/vedio.mp4")

# vedio is sequence of images
while True:
    success,img=cap.read()
    cv2.imshow("vedio",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break'''

#camera
'''
cap=cv2.VideoCapture(0)
cap.set(10,100)# brightness
# vedio is sequence of images
while True:
    success,img=cap.read()
    cv2.imshow("vedio",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break'''


#grayImage
'''
img=cv2.imread("Resources/photo.jpeg")
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Output",grayscale);
cv2.waitKey(0);'''

#blurimage
'''
img=cv2.imread("Resources/photo.jpeg")

imageblur=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Output",img);
cv2.waitKey(0);'''

#egde detector
'''
img=cv2.imread("Resources/photo.jpeg")
imCanny=cv2.Canny(img,100,100)
cv2.imshow("Output",imCanny);
cv2.waitKey(0);
'''

#image dialation

img=cv2.imread("Resources/photo.jpeg")
imCanny=cv2.Canny(img,100,100)
cv2.imshow("Outputcanny",imCanny);
kernel=np.ones((8,8),np.uint8)
imagedialation=cv2.dilate(imCanny,kernel,iterations=115)
cv2.waitKey(0);