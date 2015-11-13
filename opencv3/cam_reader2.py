import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame (original)', frame)
    cv2.imshow('frame (grey)', frame_grey)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('messigray.png', frame)
        cv2.imwrite('messigray_grey.png', frame_grey)

# When everything done, release the capture
cap.release()

cv2.destroyAllWindows