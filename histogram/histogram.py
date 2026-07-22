import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images.jpg")
cv2.imshow("images.jpg",img)


blank= np.zeros(img.shape[:2],dtype='uint8')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",gray)



circle = cv2.circle(blank, (img.shape[1]//2,img.shape[0]//2),150,255,-1)

# mask = cv2.bitwise_and(gray, gray,mask=circle)
# cv2.imshow("mask", mask)

# gray_hist = cv2.calcHist([gray], [0],mask,[256], [0,256])

plt.figure()
plt.title("Histogram")
plt.xlabel("blabla")
plt.ylabel("###")

#plt.plot(gray_hist)
#plt.xlim(0,256)
#plt.show()


# renkli histogram

color = ("b","g","r")
for i , col in enumerate(color):
    hist= cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()


cv2.waitKey()
