import cv2
import numpy as np
print("Packaged Imported")
kernel = np.ones((5,5),np.uint8)

img = cv2.imread("/home/ubuntu/bia4.jpg")
#imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgSave = cv2.Canny(img, 100,100)


cv2.imwrite("/home/ubuntu/biaGray1.jpg",imgSave)

