import cv2
import numpy
import matplotlib.pyplot as plot

kernel = numpy.ones((5, 5), numpy.uint8) # Reference unitary matrix

imageRegular = cv2.imread("Resources/lisa.png")
print(imageRegular.shape)

size = (250, 300) # W & H

imageResized = cv2.resize(imageRegular, size)
imageRegular = imageResized
imageGray = cv2.cvtColor(imageRegular, cv2.COLOR_RGB2GRAY)
imageBlur = cv2.GaussianBlur(imageRegular, (9, 9), 0)
imageCanny = cv2.Canny(imageRegular, 200, 350)
imageDilated = cv2.dilate(imageRegular, kernel, iterations=1)
imageEroded = cv2.erode(imageRegular, kernel, iterations=1)
imageCropped = imageRegular[200:5400, 50:350]

matrix0s = numpy.zeros((500, 500, 3), numpy.uint8)
shape = matrix0s        # Black
shape[:] = 255, 0, 0    # Blue (BGR)

cv2.line(shape, (0, 0), (200, 200), (0, 0, 255), 3)
cv2.rectangle(shape, (0, 0), (100, 200), (255, 0, 255), 2)
# cv2.rectangle(imageRegular, (0, 0), (100, 200), (0, 255, 255), cv2.FILLED)
cv2.circle(shape, (250, 250), 30, (0, 255, 0), 4)
                  # position  radius  color  thickness
cv2.putText(imageRegular, "Issa 'lisa", (100, 150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.2, (0, 50, 255), 2)
cv2.putText(shape, "Issa shape", (200, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.3, (50, 100, 255), 2)
                    # text         position              font                size     color    thickness
cv2.imshow("Original", imageRegular)
cv2.imshow("Image Output", imageCropped)

cv2.imshow("Shape Output", shape)
cv2.waitKey(0)
