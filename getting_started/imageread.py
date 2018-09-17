import numpy as np
import cv2
# load a color image in grayscale
img = cv2.imread('../images/Stanley_Camo.jpg', 0)
#print(img)
#Resize
# imresize = cv2.resize(img, (800, 640))

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()