# PPE Detection System

YOLO kullanılarak kamera üzerinden iş güvenliği ekipmanlarının tespit edildiği bir bilgisayarlı görü projesidir.

## Proje Hakkında

Bu projede kamera görüntüsü üzerinden kişilerin aşağıdaki iş güvenliği ekipmanlarını kullanıp kullanmadığı tespit edilir:

- Hardhat
- Mask
- Safety Vest

Ayrıca ekipmanların eksik olup olmadığı da tespit edilir:

- NO-Hardhat
- NO-Mask
- NO-Safety Vest

## Kullanılan Teknolojiler

- Python
- YOLO (Ultralytics)
- OpenCV
- CVZone

## Kurulum

Gerekli kütüphaneleri yüklemek için:

```bash
pip install ultralytics opencv-python cvzone

Bu proje eğitim ve bilgisayarlı görü öğrenme amacıyla geliştirilmiştir.
Bu proje hazırlanırken aşağıdaki YouTube videosu referans alınmış ve takip edilmiştir:

https://www.youtube.com/watch?v=WgPbbWmnXJ8&t