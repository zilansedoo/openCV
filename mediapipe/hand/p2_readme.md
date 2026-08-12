# Hill Climb Racing - Hand Control

Bu projede **OpenCV ve MediaPipe** kullanarak kameradaki el hareketleriyle Hill Climb Racing oyununu kontrol etmeye çalıştım.

Normalde klavye ile oynanan oyunda, elimizi kullanarak gaz ve fren yapıyoruz.

## Kullanılan Teknolojiler

- Python
- OpenCV
- MediaPipe

## Nasıl Çalışıyor?

Program kamerayı açıyor ve MediaPipe ile elimizi algılıyor.

Daha sonra elimizdeki parmakların açık olup olmadığı kontrol ediliyor.

Kontroller şu şekilde:

| El hareketi | Kontrol |
|---|---|
| 0 parmak | Fren |
| 5 parmak | Gaz |


Örneğin elimizi tamamen açtığımızda:5 parmak → GAS
Elinizi yumruk yaptığımızda: 0 parmak → BRAKE

El Landmarkları
tipId = [4, 8, 12, 16, 20]
Bu değerler baş parmak, işaret parmağı, orta parmak, yüzük parmağı ve serçe parmağını temsil ediyor.


Gerekli kütüphaneleri yüklemek için:
pip install opencv-python mediapipe
(ayrıca projede klavye tuşlarını kontrol etmek için p2_directkeys.py dosyasını kullandım.)


**Proje Görüntüsü**
Program çalıştığında kamera açılıyor ve elimdeki hareket MediaPipe tarafından algılanıyor.
Ekranda hareketin GAS veya BRAKE olduğu da gösteriliyor.

**Öğrendiklerim**
-OpenCV ile kamera kullanmayı
-MediaPipe ile el algılamayı
-El landmarklarını kullanmayı
-Parmak saymayı
-Koşullar ve döngüler kullanmayı
-Python ile klavye tuşlarını kontrol etmeyi

Windows kullanırken oyunu indirdiğim link:   https://apps.microsoft.com/detail/9wzdncrdcwk8?hl=en-EN&gl=EN

Projeyi yaparken kullandığım tutorial:   https://www.youtube.com/watch?v=ZBtk3GmJMTE&list








