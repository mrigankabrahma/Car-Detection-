import cv2

# capture frames from a video
cap = cv2.VideoCapture(r'C:\Users\Microsoft\Desktop\New folder (7)\Car-Detection-Basic-Open-CV-master\carv.mp4')

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier(r'C:\Users\Microsoft\Desktop\New folder (7)\Car-Detection-Basic-Open-CV-master\carx.xml')

# loop runs if capturing has been initialized.
while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2
    cv2.imshow('sKSama', frames )
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()
