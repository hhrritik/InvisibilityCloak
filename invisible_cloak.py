import cv2
import numpy as np

cap = cv2.VideoCapture(0)

back = cv2.imread("./image.jpg")

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # convert rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv",hsv)

        bgr = np.uint8([[[0, 0 , 255]]])
        hsv_clr = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        # print(hsv_green)
        # to get the hsv value of red

        #threshold the hsv value to get only red color

        lower = np.array([0, 100 , 100])
        upper = np.array([20, 255, 255])

        mask = cv2.inRange(hsv, lower, upper)
       # cv2.imshow("mask", mask)


        part1 = cv2.bitwise_and(back, back, mask=mask)
      #  cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)


        part2 = cv2.bitwise_and(frame,frame,mask=mask)
       # v2.imshow("part2" ,part2)
        cv2.imshow("cloak", part1 + part2)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
