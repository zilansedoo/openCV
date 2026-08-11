# OpenCV ile Araba Tespiti

Bu projede OpenCV kullanılarak bir video içerisindeki arabaların tespit edilmesi üzerine çalışılmıştır.

Öncelikle `haarcascade_car.xml` dosyası kullanılarak araba tespit modeli programa dahil edilmiştir. Daha sonra `cars.mp4` videosu okunarak her kare üzerinde işlem yapılmıştır.

Video kareleri gri tonlamaya dönüştürülmüş ve `detectMultiScale()` fonksiyonu kullanılarak görüntüdeki arabalar tespit edilmiştir. Tespit edilen arabaların etrafına dikdörtgen çizilmiş ve üzerlerine **"Araba"** yazısı eklenmiştir.

## Kullanılan Kütüphane

- OpenCV

## Kullanılan Fonksiyonlar

- `cv2.CascadeClassifier()` → Araba tespit modelini yükleme
- `cv2.VideoCapture()` → Video dosyasını okuma
- `cv2.cvtColor()` → Görüntüyü gri tonlamaya çevirme
- `detectMultiScale()` → Araçları tespit etme
- `cv2.rectangle()` → Tespit edilen araçların etrafına kutu çizme
- `cv2.putText()` → Görüntü üzerine yazı ekleme
- `cv2.imshow()` → Video görüntüsünü ekranda gösterme

## Çalışma Mantığı

1. Araba tespit modeli yüklenir.
2. Video dosyası açılır.
3. Videonun her karesi okunur.
4. Kare gri tonlamaya dönüştürülür.
5. Görüntüdeki arabalar tespit edilir.
6. Tespit edilen arabaların etrafına kutu çizilir.
7. Araçların üzerine "Araba" yazısı eklenir.
8. `q` tuşuna basıldığında program sonlandırılır.

## Kullanılan Dosyalar

- `haarcascade_car.xml` → araba tespit modeli
- `cars.mp4` → üzerinde çalışma yapılan video

Bu çalışma ile Haar Cascade kullanarak video içerisindeki araçları tespit etme ve tespit edilen nesneleri görüntü üzerinde işaretleme işlemleri öğrenilmiştir.