import cv2
import mediapipe as mp
import pyautogui
import math
import time

# AYARLAR

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# mouse hareketinin daha yumuşak olması için
SMOOTHING = 7

# tıklama için parmaklar arası maksimum mesafe
CLICK_DISTANCE = 35

# --------------------------------------------------
# MOUSE

screen_width, screen_height = pyautogui.size()

pyautogui.PAUSE = 0.01

# --------------------------------------------------
# MEDIAPIPE

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7)

# --------------------------------------------------
# KAMERA
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

# önceki mouse pozisyonu
prev_x = 0
prev_y = 0

# tıklama kontrolü
click_cooldown = 0

print("Sanal Mouse başlatıldı.")
print("Q = Çıkış")

# --------------------------------------------------
# ANA DÖNGÜ
while True:

    success, frame = cap.read()

    if not success:
        print("Kamera görüntüsü alınamadı.")
        break

    # aynala
    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:
            # işaret parmağı ucu
            index_finger = hand_landmarks.landmark[
                mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # başparmak ucu
            thumb = hand_landmarks.landmark[
                mp_hands.HandLandmark.THUMB_TIP]

            # Ekran koordinatlarına dönüştür
            camera_x = int(index_finger.x * CAMERA_WIDTH)
            camera_y = int(index_finger.y * CAMERA_HEIGHT)

            # ------------------------------------------
            # MOUSE KOORDİNAT

            mouse_x = int(index_finger.x * screen_width)

            mouse_y = int( index_finger.y * screen_height )

            # Smooth hareket
            smooth_x = prev_x + ( mouse_x - prev_x) / SMOOTHING

            smooth_y = prev_y + (  mouse_y - prev_y) / SMOOTHING

            pyautogui.moveTo( int(smooth_x),  int(smooth_y))

            prev_x = smooth_x
            prev_y = smooth_y

            # ------------------------------------------
            # PARMAK UÇLARINI ÇİZ
            # ------------------------------------------

            ix = int(index_finger.x * CAMERA_WIDTH)
            iy = int(index_finger.y * CAMERA_HEIGHT)

            tx = int(thumb.x * CAMERA_WIDTH)
            ty = int(thumb.y * CAMERA_HEIGHT)

            cv2.circle( frame,(ix, iy), 10, (255, 0, 255), cv2.FILLED  )

            cv2.circle(frame,(tx, ty), 10, (0, 255, 255), cv2.FILLED )

            # ------------------------------------------
            # BAŞPARMAK + İŞARET PARMAĞI MESAFESİ
            # ------------------------------------------

            distance = math.sqrt((ix - tx) ** 2 + (iy - ty) ** 2 )

            # Parmakları birleştirince çizgi çiz
            cv2.line(frame, (ix, iy),(tx, ty),(255, 255, 255),2  )

            # ------------------------------------------
            # SOL TIK
    

            if distance < CLICK_DISTANCE:
                cv2.putText( frame, "CLICK",   (20, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 3 )

                if time.time() > click_cooldown:
                    pyautogui.click()
                    click_cooldown = ( time.time() + 0.5 )

            # ------------------------------------------
            # ELİ ÇİZ
            mp_draw.draw_landmarks( frame, hand_landmarks,mp_hands.HAND_CONNECTIONS )

    # ------------------------------------------
    # EKRANA BİLGİ
   

    cv2.putText(frame,"Virtual Mouse", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255, 255, 255), 2)

    cv2.putText( frame,"Index Finger = Move", (20, 135), cv2.FONT_HERSHEY_SIMPLEX,0.6,(255, 255, 255),2 )

    cv2.putText(frame,"Pinch = Click",(20, 165), cv2.FONT_HERSHEY_SIMPLEX,0.6,(255, 255, 255), 2 )

    cv2.putText( frame,"Q = Exit", (20, 195),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255),2 )


    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
hands.close()