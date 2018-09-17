import numpy as np
import cv2

img = cv2.imread('../images/Stanley_Camo.jpg', 0)
cv2.imwrite(r'../images/Stanley_Camo_02.png', img)