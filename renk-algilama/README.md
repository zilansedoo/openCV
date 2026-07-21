# OpenCV ile HSV Renk Tespiti

Bu projede OpenCV kullanılarak gerçek zamanlı renk tespiti uygulaması geliştirilmiştir. Kamera görüntüsü HSV (Hue, Saturation, Value) renk uzayına dönüştürülerek belirlenen renk aralığındaki nesneler maskeleme yöntemiyle tespit edilmektedir.

## Özellikler

- Kameradan gerçek zamanlı görüntü alma
- BGR renk uzayını HSV renk uzayına dönüştürme
- Trackbar kullanarak HSV değerlerini anlık değiştirme
- Belirlenen renk aralığı için maske oluşturma
- Seçilen renkleri filtreleyerek ekranda gösterme
- Orijinal görüntü, HSV görüntüsü ve filtrelenmiş sonucu aynı anda görüntüleme

## Kullanılan Kütüphaneler

- OpenCV (`cv2`)
- NumPy (`numpy`)

## Kullanılan Fonksiyonlar

- `cv2.VideoCapture()`
- `cv2.cvtColor()`
- `cv2.createTrackbar()`
- `cv2.getTrackbarPos()`
- `cv2.inRange()`
- `cv2.bitwise_and()`
- `cv2.imshow()`
- `cv2.waitKey()`

## Projenin Amacı

Bu çalışma, OpenCV'de HSV renk uzayının çalışma mantığını öğrenmek, farklı renk aralıklarını tespit etmek ve gerçek zamanlı görüntü işleme uygulamaları geliştirmek amacıyla hazırlanmıştır.
