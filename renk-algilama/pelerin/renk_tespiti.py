import cv2 
import numpy as np 

cap = cv2.VideoCapture(0) 
# arka plan kaydet 
for i in range(30): 
    ret, background = cap.read() 
    background = np.flip(background, axis=1) 
    # renk seçilsin 
    cv2.namedWindow("Trackbars") 
    cv2.createTrackbar("L-H", "Trackbars", 20, 179, lambda x: None) 
    cv2.createTrackbar("L-S", "Trackbars", 100, 255, lambda x: None) 
    cv2.createTrackbar("L-V", "Trackbars", 100, 255, lambda x: None) 
    cv2.createTrackbar("U-H", "Trackbars", 40, 179, lambda x: None) 
    cv2.createTrackbar("U-S", "Trackbars", 255, 255, lambda x: None) 
    cv2.createTrackbar("U-V", "Trackbars", 255, 255, lambda x: None) 
    while True: 
        ret, frame = cap.read() 
        frame = np.flip(frame, axis=1) 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
       
        l_h = cv2.getTrackbarPos("L-H", "Trackbars") 
        l_s = cv2.getTrackbarPos("L-S", "Trackbars") 
        l_v = cv2.getTrackbarPos("L-V", "Trackbars") 
        u_h = cv2.getTrackbarPos("U-H", "Trackbars") 
        u_s = cv2.getTrackbarPos("U-S", "Trackbars") 
        u_v = cv2.getTrackbarPos("U-V", "Trackbars") 
       
        lower = np.array([l_h, l_s, l_v]) 
        upper = np.array([u_h, u_s, u_v]) 
 
        mask = cv2.inRange(hsv, lower, upper) 
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8)) 
      
        mask_inv = cv2.bitwise_not(mask) 
        person = cv2.bitwise_and(frame, frame, mask=mask_inv) 
        cloak = cv2.bitwise_and(background, background, mask=mask) 
       
        result = cv2.addWeighted(person, 1, cloak, 1, 0)
        cv2.imshow("Result", result) 
        cv2.imshow("Mask", mask) 
        if cv2.waitKey(1) == 27: 
            break 
cap.release() 
cv2.destroyAllWindows()