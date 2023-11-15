import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, image = cap.read()
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original Image', image)
cv2.imshow('Red Only', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
