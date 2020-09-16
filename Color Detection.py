import cv2
import numpy
import matplotlib.pyplot as plot


def refresh(x):
    pass


cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 550, 250)
cv2.createTrackbar("Hue Min", "Trackbar", 101, 179, refresh)
cv2.createTrackbar("Hue Max", "Trackbar", 114, 179, refresh)
cv2.createTrackbar("Saturation Min", "Trackbar", 0, 255, refresh)
cv2.createTrackbar("Saturation Max", "Trackbar", 255, 255, refresh)
cv2.createTrackbar("Value Min", "Trackbar", 180, 255, refresh)
cv2.createTrackbar("Value Max", "Trackbar", 255, 255, refresh)

image = cv2.imread("Resources/tree.png")

while(True):
    imageRegular = cv2.resize(image, (256, 256))
    imageHSV = cv2.cvtColor(imageRegular, cv2.COLOR_BGR2HSV)

    hueMin = cv2.getTrackbarPos("Hue Min", "Trackbar")
    hueMax = cv2.getTrackbarPos("Hue Max", "Trackbar")
    saturationMin = cv2.getTrackbarPos("Saturation Min", "Trackbar")
    saturationMax = cv2.getTrackbarPos("Saturation Max", "Trackbar")
    valueMin = cv2.getTrackbarPos("Value Min", "Trackbar")
    valueMax = cv2.getTrackbarPos("Value Max", "Trackbar")

    print(hueMin, hueMax, saturationMin, saturationMax, valueMin, valueMax)

    low = numpy.array([hueMin, saturationMin, valueMin])
    high = numpy.array([hueMax, saturationMax, valueMax])
    masking = cv2.inRange(imageHSV, low, high)

    maskedImage = cv2.bitwise_and(imageRegular, imageRegular, mask=masking)

    cv2.imshow("Original", imageRegular)
    cv2.imshow("HSV", imageHSV)
    cv2.imshow("Masking", masking)
    cv2.imshow("Masked", maskedImage)
    cv2.waitKey(1)
