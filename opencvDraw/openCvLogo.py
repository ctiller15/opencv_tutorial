import numpy as np
import cv2

circleone = (0, 0, 255)
circleTwo = (0, 255, 0)
circleThree = (255, 0,0)
blackCircle = (0, 0, 0)
img = np.zeros((512, 512, 3), np.uint8)

# Red circle
img = cv2.ellipse(img,(256,128),(50,50),120,0,300,circleone,-1)
img = cv2.ellipse(img, (256, 128), (20, 20), 0, 0, 360, blackCircle, -1)

# Green circle
img = cv2.ellipse(img,(192,256),(50,50),0,0,300,circleTwo,-1)
img = cv2.ellipse(img, (192, 256), (20, 20), 0, 0, 360, blackCircle, -1)

# Blue circle
img = cv2.ellipse(img,(320,256),(50,50),-60,0,300,circleThree,-1)
img = cv2.ellipse(img, (320, 256), (20, 20), 0, 0, 360, blackCircle, -1)

# Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4,(255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()