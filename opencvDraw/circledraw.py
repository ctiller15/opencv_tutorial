import numpy as np
import cv2

# Drawing the circle.
img = np.zeros((512, 512, 3), np.uint8)
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()