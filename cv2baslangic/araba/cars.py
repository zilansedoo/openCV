import cv2

cascade_path = "haarcascade_car.xml"
car_cascade = cv2.CascadeClassifier(cascade_path)

if car_cascade.empty():
    print(
        f"Hata: '{cascade_path}' okunamadı. Dosya adını veya konumunu kontrol edin."
    )
    exit()

video_path = "cars.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale( gray, 1.1, 3, minSize=(20, 20))

    # araçları çerçeve içine al
    for x, y, w, h in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText( frame, "Araba", (x, y - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),1,)

    cv2.imshow("Araba Tespiti", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()