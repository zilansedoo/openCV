# Hand Gesture - Love You

**MediaPipe** çalışırken geliştirdiğim ilk kod. 

Bu proje, **OpenCV** ve **MediaPipe** kullanarak kameradaki el hareketlerini algılar. Kullanıcı belirli sayıda parmağını gösterdiğinde geri sayım ilerler ve geri sayım tamamlandığında ekranda **"LOVE YOU <3"** mesajı gösterilir.

## Kullanılan Teknolojiler

- Python
- OpenCV
- MediaPipe

## Kullanılan Kütüphaneler

```bash
pip install opencv-python mediapipe

Program bilgisayarın kamerasını açar ve görüntüyü gerçek zamanlı olarak işler.

MediaPipe Hands kullanılarak görüntüdeki el ve el üzerindeki landmark noktaları tespit edilir.

Parmak uçlarının ID değerleri:
tipId = [4, 8, 12, 16, 20]
-Baş parmak
-İşaret parmağı
-Orta parmak
-Yüzük parmağı
-Serçe parmak


Kullanıcı hedeflenen parmak sayısını gösterdiğinde sayaç azalır: 5 → 4 → 3 → 2 → 1 → 0
Sayaç sıfır olduğunda "love_you= true" olur.
Geri sayım tamamlandığında ekranda: "LOVE YOU <3" mesajı gösterilir.