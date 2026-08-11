# OpenCV ile Gerçek Zamanlı Mavi Nesne Tespiti

Bu projede OpenCV ve NumPy kullanılarak kamera görüntüsü üzerinden gerçek zamanlı mavi nesne tespiti yapılmıştır.

Kamera görüntüsü HSV renk uzayına dönüştürülerek belirlenen mavi renk aralığı tespit edilmiştir. Daha sonra tespit edilen renk için maske oluşturulmuş ve `findContours()` fonksiyonu kullanılarak renkli nesnenin sınırları bulunmuştur.

Bulunan en büyük nesnenin etrafına bir dikdörtgen çizilmiş, nesnenin merkez koordinatları hesaplanarak görüntü üzerine yazdırılmıştır.

## Kullanılan Kütüphaneler

- OpenCV
- NumPy

## Kullanılan OpenCV Fonksiyonları

- `cv2.VideoCapture()` → Kameradan görüntü alma
- `cv2.cvtColor()` → BGR görüntüyü HSV renk uzayına dönüştürme
- `cv2.inRange()` → Belirlenen renk aralığı için maske oluşturma
- `cv2.bitwise_and()` → Maskeyi görüntüye uygulama
- `cv2.findContours()` → Nesnenin sınırlarını bulma
- `cv2.contourArea()` → Konturun alanını hesaplama
- `cv2.boundingRect()` → Nesneyi çevreleyen dikdörtgeni bulma
- `cv2.rectangle()` → Nesnenin etrafına dikdörtgen çizme
- `cv2.putText()` → Görüntü üzerine yazı ve koordinat ekleme
- `cv2.imshow()` → Görüntüyü ekranda gösterme

## Projenin Çalışma Mantığı

1. Kameradan görüntü alınır.
2. Görüntü BGR renk uzayından HSV renk uzayına dönüştürülür.
3. Belirlenen HSV aralığındaki mavi renkler tespit edilir.
4. Tespit edilen renkler için maske oluşturulur.
5. Maskedeki konturlar bulunur.
6. En büyük kontur seçilir.
7. Nesnenin etrafına dikdörtgen çizilir.
8. Nesnenin merkez koordinatları hesaplanır.
9. Nesnenin adı ve koordinatları görüntü üzerine yazdırılır.

## Görüntüde Gösterilen Bilgiler

Tespit edilen nesnenin:

- Etrafına kırmızı bir dikdörtgen çizilir.
- Üzerine **"mavi nesne"** yazılır.
- Alt kısmında nesnenin merkez koordinatları gösterilir.

Örnek:

```text
mavi nesne
┌──────────────┐
│      🔵      │
└──────────────┘
X: 320, Y: 240
```

## Projenin Amacı

Bu proje, OpenCV kullanarak gerçek zamanlı renk tespiti, kontur analizi, nesne koordinatlarının bulunması ve görüntü üzerine bilgi ekleme konularını uygulamalı olarak öğrenmek amacıyla hazırlanmıştır.