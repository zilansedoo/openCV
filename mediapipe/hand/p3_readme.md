# El Hareketleriyle Zaman Ayarlı Kamera

Bu proje, **OpenCV** ve **cvzone HandTrackingModule** kullanarak el hareketleriyle çalışan basit bir zaman ayarlı kamera uygulamasıdır.

Kamera görüntüsü üzerinden el hareketleri algılanır ve gösterilen parmak sayısına göre belirli bir süre geri sayım yapılır. Süre tamamlandığında kameradan otomatik olarak fotoğraf çekilir ve bilgisayara kaydedilir.

## Kullanılan Kütüphaneler

* `opencv-python` — Kamera görüntüsünü almak, ekrana görüntü vermek ve fotoğraf kaydetmek için.
* `cvzone` — El ve parmak hareketlerini kolayca algılamak için.
* `time` — Geri sayım süresini kontrol etmek için.
* `random` — Kaydedilen fotoğrafa rastgele bir dosya adı vermek için.

## Nasıl Çalışır?

Program bilgisayarın kamerasını açar ve görüntü içerisindeki eli algılar. Kullanıcı bir el hareketi yaptığında, gösterilen parmak sayısına göre farklı bir geri sayım başlatılır.

| Parmak Hareketi | Geri Sayım |
| --------------- | ---------: |
| ☝️ 1 parmak     |   2 saniye |
| ✌️ 2 parmak     |   4 saniye |
| 3 parmak        |   6 saniye |
| 4 parmak        |   8 saniye |
| 🖐️ 5 parmak    |  10 saniye |

Geri sayım sırasında ekranda **Timer** değeri gösterilir. Sayaç tamamlandığında mevcut kamera görüntüsü bir `.jpg` dosyası olarak kaydedilir.

Fotoğrafın adı şu formatta oluşturulur:
```text
camera42.jpg
```
Buradaki sayı rastgele olarak `1-100` arasında belirlenir.

## Kullanım

1. Programı çalıştırın.
2. Kamera açılacaktır.
3. Kameraya elinizi gösterin.
4. İstediğiniz parmak hareketini yapın.
5. Seçilen süre kadar geri sayım yapılacaktır.
6. Süre tamamlandığında fotoğraf otomatik olarak çekilecektir.
7. Fotoğraf programın çalıştığı klasöre `.jpg` olarak kaydedilecektir.

