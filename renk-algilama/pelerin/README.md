# Görünmez Pelerin (OpenCV)

Bu proje, **Python** ve **OpenCV** kullanarak görüntü işleme öğrenmek amacıyla hazırlanmış **basit bir deneme projesidir**.

Program ilk olarak kameradan arka planı kaydeder. Daha sonra HSV renk aralığı kullanılarak seçilen renk tespit edilir ve bu alanlar kayıtlı arka plan ile değiştirilerek temel bir "görünmez pelerin" efekti oluşturulur.

## Özellikler

- Kameradan arka plan kaydı alma
- HSV trackbar ile renk seçebilme
- Gerçek zamanlı renk maskeleme
- Gürültüyü azaltmak için temel morfolojik filtreleme
- Sonuç ve maske görüntüsünü anlık olarak gösterme

## Gereksinimler

- Python 3.x
- OpenCV
- NumPy

Gerekli kütüphaneleri yüklemek için:

```bash
pip install opencv-python numpy
```

## Çalıştırma

```bash
python main.py
```

## Kullanım

- Trackbar'ları kullanarak pelerinin rengini ayarlayın.
- Çıkış yapmak için **ESC** tuşuna basın.

## Not

Bu proje tamamen **öğrenme amaçlı hazırlanmış basit bir deneme çalışmasıdır.** Efektin başarısı ortam ışığına ve seçilen rengin doğru ayarlanmasına bağlıdır.