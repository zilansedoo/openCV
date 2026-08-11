import cv2

# Yüz algılama modeli
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt.xml"
)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Yüzleri bul
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:

        face = img[y:y+h, x:x+w] #yüzün bulunduğu alan

        # yüzü bulanıklaştır
        blur_face = cv2.GaussianBlur(face, (101,101),0)

        # bulanık yüzü geri koy
        img[y:y+h, x:x+w] = blur_face
        
        cv2.putText(img, "yasak", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(0,0,255),1)

    cv2.imshow("Face Blur", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()