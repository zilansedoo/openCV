import cv2
from cvzone.HandTrackingModule import HandDetector
import time


detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv2.VideoCapture(0)

aktif = False
foto_no = 1


# fotoğraf çekme
def fotograf_cek():
    global foto_no

    ret, frame = video.read()
    if ret:
        dosya_adi = "foto_" + str(foto_no) + ".jpg"
        cv2.imwrite(dosya_adi, frame)
        print("fotoğraf çekildi: ", dosya_adi)
        foto_no += 1


# zamanlayici
def timer_cek(sure):

    baslangic = time.time()
    while True:

        ret, frame = video.read()

        gecen = int(time.time() - baslangic)
        kalan = sure - gecen

        cv2.rectangle(frame,(0, 0),(300, 70),(20, 20, 20), -1)

        cv2.putText( frame,"Timer: " + str(kalan), (30, 50), cv2.FONT_HERSHEY_SIMPLEX,  1,(255, 255, 255), 2)

        cv2.imshow("El Kontrollu Kamera", frame)

        if kalan <= 0:
            fotograf_cek()
            break
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

while True:
    ret, frame = video.read()

    frame = cv2.flip(frame, 1)

    hands, frame = detector.findHands(frame,draw=True,flipType=False)

    #el bulursa
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        toplam = fingers.count(1)

        # ekranda parmak sayısını göster
        cv2.putText( frame,"Parmak: " + str(toplam),(20, 80),cv2.FONT_HERSHEY_SIMPLEX,  0.7,(255, 255, 255),2)


        # -------------------------------- aç
        if toplam == 5:
            aktif = True

            cv2.putText( frame,"SISTEM AKTIF",(20, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0, 255, 0), 2)

        # -------------------------------- kapa

        elif toplam == 0:

            aktif = False
            cv2.putText(frame, "SISTEM DURDU",(20, 40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0, 0, 255),2)


        # -------------------------------- aktifse
        elif aktif:
            cv2.putText(frame,"SISTEM AKTIF",(20, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0, 255, 0),2 )

            # 1 parmak
            if toplam == 1:
                fotograf_cek()
                time.sleep(1)
            # 2 parmak
            elif toplam == 2:
                timer_cek(5)
            # 3 parmak
            elif toplam == 3:
                timer_cek(10)


        # ----------------------------

        else:
           cv2.putText( frame,  "SISTEM DURDU",(20, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0, 0, 255),2 )


    else:

        if aktif:

            cv2.putText( frame,"SISTEM AKTIF", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0, 255, 0), 2)

        else:

            cv2.putText(frame, "SISTEM DURDU", (20, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0, 0, 255),  2)


    cv2.imshow("El Kontrollu Kamera", frame)


    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break


video.release()
cv2.destroyAllWindows()