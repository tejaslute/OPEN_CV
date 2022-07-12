import cv2
import numpy as np

img = cv2.imread("1.jpeg", cv2.IMREAD_GRAYSCALE)

laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
if laplacian_var < 5:
    print("Image blurry")
    cv2.putText(img, "BLUR IMAGE", (400, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (1, 150, 1), 1)
else:
    print("Cleared image")

print(laplacian_var)

cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()