import cv2
import numpy
import matplotlib.pyplot as plot


def getContours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if (area > 500):
            cv2.drawContours(imageContours, contour, -1, (255, 0, 0), 3)
        # perimeter = cv2.arcLength(contour, True)
        # print(f"The perimeter is {perimeter}")


imageRegular = cv2.imread("Resources/shapes.png")
imageRegular = cv2.resize(imageRegular, (250, 250))

imageGray = cv2.cvtColor(imageRegular, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imageGray, (7, 7), 1)
imageCanny = cv2.Canny(imageBlur, 80, 150)

imageContours = imageRegular.copy()
getContours(imageCanny)

cv2.imshow("Original", imageRegular)
cv2.imshow("Gray", imageGray)
cv2.imshow("Blurred", imageBlur)
cv2.imshow("Canny", imageCanny)
cv2.imshow("Final", imageContours)
cv2.waitKey(0)
