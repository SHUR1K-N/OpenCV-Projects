import cv2

faceCascade = cv2.CascadeClassifier("rsc/xml/haarcascade_frontalface_default.xml")
image = cv2.imread("rsc/people.jpg")
image = cv2.resize(image, (700, 500))
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imageGray, 1.1, 6)

for (x, y, width, height) in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)

cv2.imshow("Final", image)
cv2.waitKey(0)
