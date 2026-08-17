import cv2

kamera = cv2.VideoCapture(0)

qr = cv2.QRCodeDetector()

while True:

    ret, frame = kamera.read()

    frame = cv2.flip(frame, 1)

    data, kordinat, _ = qr.detectAndDecode(frame)

    if kordinat is not None:
        kordinat = kordinat.astype(int) #tam sayı çevir
        for i in range(4):
            cv2.line( frame,
                tuple(kordinat[0][i]),
                tuple(kordinat[0][(i + 1) % 4]),(0, 255, 0), 3)
    if data:
        print("QR:", data)
        cv2.putText(frame,data, (20, 50), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 0), 2 )

    cv2.imshow("QR Okuyucu", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()