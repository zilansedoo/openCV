import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipId = [4, 8, 12, 16, 20]
last_total = -1
countdown = 5
love_you = False

video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while True:
        ret, image = video.read()
        if not ret:
            break
         
        image = cv2.flip(image, 1)
        
        h, w, c = image.shape
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        lmList = []
        
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                      
                mp_draw.draw_landmarks(
                    image, 
                    hand_landmark,
                    mp_hand.HAND_CONNECTIONS,
                    mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
                    mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2)
                )
        
        fingers = []
        if len(lmList) != 0:
            # Baş parmak kontrolü (Sağ/Sol el uyumu için x ekseni)
            if lmList[tipId[0]][1] > lmList[tipId[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
                
            # diğer 4 parmak kontrolü (y ekseni)
            for id in range(1, 5):
                if lmList[tipId[id]][2] < lmList[tipId[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                    
            total = fingers.count(1)
            
            # geri sayım mantığı (5 -> 0)
            if total == countdown and total != last_total:
                    countdown -= 1
                    last_total = total
                
                    if countdown == 0:
                        love_you = True
            elif total != countdown:
                last_total = -1
        
        # --- ARAYÜZ  ---
        
        # yarı saydam arkaplan kutusu
        overlay = image.copy()
        cv2.rectangle(overlay, (20, 20), (380, 110), (0, 0, 0), -1)
        alpha = 0.6
        image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
        
        # sayaç bilgisi
        if not love_you:
            cv2.putText(image, f"Target Fingers: {countdown}", (35, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, "Show the target finger count!", (35, 95),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1, cv2.LINE_AA)
        
        # Love You mesajı 
        if love_you:
            #kutu
            cv2.rectangle(overlay, (w // 2 - 220, h // 2 - 70), (w // 2 + 220, h // 2 + 70), (0, 0, 0), -1)
            image = cv2.addWeighted(overlay, 0.7, image, 0.3, 0)
            
            cv2.putText(image, "LOVE YOU <3", 
                        (w // 2 - 200, h // 2 + 15), 
                        cv2.FONT_HERSHEY_DUPLEX, 
                        1.5, 
                        (0, 10, 255),  
                        3, 
                        cv2.LINE_AA)
        
        cv2.imshow("love u", image)
        
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

video.release()
cv2.destroyAllWindows()