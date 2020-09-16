import cv2
import numpy
import matplotlib.pyplot as plot

image1 = cv2.imread("Resources/tree.png")
image2 = cv2.imread("Resources/tree.png")

imageHorizontal = numpy.hstack((image1, image2))
imageVertical = numpy.vstack((image1, image2))

cv2.imshow("Horizontal", imageHorizontal)
cv2.imshow("Vertical", imageVertical)
cv2.waitKey(0)
