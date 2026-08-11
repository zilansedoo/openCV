from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *
import numpy as np 


cap= cv2.VideoCapture("cars7.mp4")

model = YOLO("yolo11n.pt")

classNames = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
    "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
    "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
    "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
    "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
    "teddy bear", "hair drier", "toothbrush"
]


mask = cv2.imread("mask.png")

#tracking
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

limits = [300, 297,673,297]
totalCount=0
counted_ids= set()

while True:
    success, img= cap.read()
    
    imgRegion= cv2.bitwise_and(img,mask)
    
    results= model(imgRegion,stream=True)
    
    detections= np.empty((0,5))
    
    for r in results: 
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2= box.xyxy[0]
            x1,y1,x2,y2= int(x1), int(y1), int(x2), int(y2)
            w,h= x2-x1,  y2-y1
            cvzone.cornerRect(img,(x1,y1,w,h),l=5,rt=5)
            
            conf= math.ceil((box.conf[0]* 100)) / 100
            cls= int(box.cls[0])
            currentClass= classNames[cls]
            
            if currentClass=="car" or currentClass =="track" or currentClass =="bus" or currentClass =="motorbike"   and conf > 0.3:
              #  cvzone.putTextRect(img, f'{currentClass} {conf}' 
               #                    , (max(0,x1) , max(35,y1))
                #                   , scale=0.6, thickness=1,offset=3 )
                
               # cvzone.cornerRect(img,(x1,y1,w,h),l=10)
              
                
                currentArray= np.array([x1,y1,x2,y2,conf])
                detections=np.vstack((detections,currentArray))
                
    resultsTracker = tracker.update(detections)
    cv2.line(img,(limits[0],limits[1]),(limits[2],limits[3]), (0,0,255),5)
    
    
    for result in resultsTracker:
        x1,y1,x2,y2,id = result
        x1,y1,x2,y2= int(x1), int(y1), int(x2), int(y2)
        
        
        w,h= x2-x1,  y2-y1
        
        cx,cy= x1+w//2, y1+h//2
     #   cvzone.cornerRect(img,(x1,y1,w,h),l=5,rt=2,colorR=(255,0,0))
        cvzone.putTextRect(img, f' {int(id)}' 
                           , (max(0,x1) , max(20,y1))
                           , scale=2, thickness=2,offset=5 )
        
        
        cv2.circle(img, (cx,cy), 5, (255,0,255),cv2.FILLED)
        
        if limits[0] < cx < limits[2]:
            if limits[1] - 30 < cy < limits[1] + 30:
                if id not in counted_ids:
                    totalCount += 1
                    counted_ids.add(id)
            
        cvzone.putTextRect(
            img,
                f'Count: {totalCount}',
                (50, 50),
                scale=2,
                thickness=2,
                offset=5)              
        
    cv2.imshow("image",img)
    cv2.imshow("mask",imgRegion)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    

cap.release()
cv2.destroyAllWindows()