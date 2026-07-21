import cv2
import numpy as np

camera= cv2.VideoCapture(0)

while True:
    ret,frame= camera.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower = np.array([90,100,100])
    upper = np.array([130,255,255])

    mask = cv2.inRange(hsv,lower,upper)
  
    res= cv2.bitwise_and(frame,frame,mask=mask)
    
    con, hie= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(con)>0:
        con = max(con,key=cv2.contourArea)
        x,y,w,h= cv2.boundingRect(con)
        merkezX= x+w //2
        merkezY= y+h //2 
        
        cv2.rectangle(frame,(x,y), (x+w,y+h), (0,0,255),2) #kare içine al
        
        cv2.putText(frame,"mavi nesne",(x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0, 0, 255), 2)  #üst  yazı
        cv2.putText(frame, f"X: {merkezX}, Y: {merkezY}",(x, y + h + 25),cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 0),2)  #alt yazı
    
    
    cv2.imshow("kare",frame)    
        
    if cv2.waitKey(1)== 27:
        break
    
    
camera.release()
cv2.destroyAllWindows()    