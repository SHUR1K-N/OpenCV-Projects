import cv2
import numpy
import matplotlib.pyplot as plot

imageRegular = cv2.imread("rsc/cards.jpg")

## To get the edge points of J card:

# plot.imshow(imageRegular)
# plot.waitforbuttonpress(0)

## 123, 533 - bottom-left of card
## 441, 782 - bottom-right of card
## 472, 136 - top-left of card
## 781, 354 - top-right of card

width = imageRegular.shape[0]
height = imageRegular.shape[1]

pointsRegular = numpy.float32([[123, 533], [441, 782], [472, 136], [781, 354]])
pointsStraighten = numpy.float32([[0, height], [width, height], [0, 0], [width, 0]])
matrix = cv2.getPerspectiveTransform(pointsRegular, pointsStraighten)
imageWarped = cv2.warpPerspective(imageRegular, matrix, (width, height))

cv2.imshow("Original", imageRegular)
cv2.imshow("Warped", imageWarped)
cv2.waitKey(0)
