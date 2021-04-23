import cv2
cap = cv2.VideoCapture(0) #this is webcam

while cap.isOpened():
    ret , back = cap.read()
     # back is what the camera is reading and ret is bascially that if a bool like whatever u r reading is successful/not
    if ret :
        cv2.imshow("image",back)
        if cv2.waitKey(10) == ord('q'):
            #save the image
            cv2.imwrite('image.jpg',back)
            break;
cap.release()
cv2.destroyAllWindows()
