import cv2
import time
import numpy as np

image = cv2.imread("bangkok.jpg")
cap = cv2.VideoCapture(0)

time.sleep(2)

while True:
    
    ret, frame = cap.read()
    print(frame)

    frame = np.flip(frame, axis = 1)

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])

    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    f = frame - res
    f = np.where(f == 0, image, f)

    
    cv2.imshow("mask", f)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()