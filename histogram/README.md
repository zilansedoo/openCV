# OpenCV ile Renkli Görüntü Histogramı

Bu projede OpenCV ve Matplotlib kullanılarak bir görüntünün renk kanallarına ait histogramlar incelenmiştir.

Öncelikle bir görüntü programa aktarılmış ve görüntünün belirli bir bölgesini seçebilmek için maske oluşturma işlemi incelenmiştir. Daha sonra görüntüde bulunan BGR (Blue, Green, Red) renk kanallarının histogramları hesaplanarak grafik üzerinde gösterilmiştir.

## Kullanılan Kütüphaneler

- OpenCV
- NumPy
- Matplotlib

## Kullanılan Fonksiyonlar

- `cv2.imread()` → Görüntü yükleme
- `cv2.imshow()` → Görüntüyü görüntüleme
- `np.zeros()` → Boş maske oluşturma
- `cv2.circle()` → Dairesel maske oluşturma
- `cv2.calcHist()` → Histogram hesaplama
- `plt.plot()` → Histogramı grafik üzerinde gösterme

## Projenin Çalışma Mantığı

1. Görüntü programa aktarılır.
2. Görüntünün boyutlarına göre boş bir maske oluşturulur.
3. Görüntünün merkezinde dairesel bir alan oluşturulur.
4. Görüntünün BGR renk kanalları ayrı ayrı incelenir.
5. Her renk kanalı için histogram hesaplanır.
6. Histogramlar Matplotlib kullanılarak grafik üzerinde gösterilir.

## Histogram Nedir?

Histogram, bir görüntüdeki piksel değerlerinin dağılımını gösteren grafiktir.

Bu projede:

- **B (Blue)** → Mavi renk kanalı
- **G (Green)** → Yeşil renk kanalı
- **R (Red)** → Kırmızı renk kanalı

ayrı ayrı incelenmiştir.

Bu çalışma ile OpenCV'de histogram oluşturma, renk kanallarını inceleme ve görüntü verilerini grafik üzerinde analiz etme konuları öğrenilmiştir.