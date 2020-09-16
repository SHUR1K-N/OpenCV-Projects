import cv2

faceCascade = cv2.CascadeClassifier("Resources/xml/haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while(True):

    returnValue, image = video.read()

    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imageGray, 1.1, 6)

    for (x, y, width, height) in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)

    cv2.imshow("Camera Feed", image)
    cv2.waitKey(60)
video.release()
cv2.destroyAllWindows()
