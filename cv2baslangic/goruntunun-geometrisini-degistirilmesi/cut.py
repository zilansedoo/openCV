import cv2
import numpy as np


img = cv2.imread("ss1.jpg")

print(img.shape)


rows ,cols= img.shape[:2]


dst_resim= np.float32([
    [0,0],  #üst sol 
    [cols-1,0],  #üst sağ
    [0,rows-1], #alt sol
    [cols-1,rows-1]])  #alt sağ


click= 0
a= []
cv2.namedWindow("img",cv2.WINDOW_NORMAL)

def draw(event,x,y,flags,param):
    global click,a
    
    if click <4:
        if event== cv2.EVENT_LBUTTONDBLCLK:
            print(click,")","x:",x,"y:",y)
            click +=1
            a.append((x,y))
        
    else:
     
        
        src = np.float32([
            [a[0][0],a[0][1]],
            [ a[1][0],a[1][1]],
            [ a[2][0],a[2][1]],
            [ a[3][0],a[3][1]]])
        click=0
        a= []
        M = cv2.getPerspectiveTransform(src, dst_resim)
        img_output3 = cv2.warpPerspective(img, M, (cols,rows))
        cv2.imshow("img_output3",img_output3)
        
    pass

cv2.setMouseCallback("img", draw)

while(1):
    cv2.imshow("img",img)
   
    if    cv2.waitKey(0) == ord("q"):
        break
cv2.destroyAllWindows()