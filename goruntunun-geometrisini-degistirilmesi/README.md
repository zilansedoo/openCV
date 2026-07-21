# OpenCV Perspektif Dönüşümü

Bu projede OpenCV kullanılarak bir görüntü üzerinde perspektif dönüşümü yapılmıştır.

Program çalıştırıldığında görüntü ekranda gösterilir. Görüntü üzerinde fare ile dört farklı noktaya çift tıklanır (sağ üst, sol üst, sağ alt ve sol alt sırasıyla) . Bu noktaların koordinatları alınarak kaynak noktalar oluşturulur.

Daha sonra:

- `cv2.getPerspectiveTransform()` ile dönüşüm matrisi oluşturulur.
- `cv2.warpPerspective()` ile görüntünün perspektifi değiştirilir.
- Elde edilen yeni görüntü ekranda gösterilir.

## Kullanılan Kütüphaneler

- OpenCV
- NumPy

## Kullanılan Fonksiyonlar

- `cv2.imread()`
- `cv2.namedWindow()`
- `cv2.setMouseCallback()`
- `cv2.getPerspectiveTransform()`
- `cv2.warpPerspective()`
- `cv2.imshow()`

## Nasıl Çalışır?

1. Görüntü yüklenir.
2. Görüntünün boyutları alınır.
3. Görüntü üzerinde dört noktaya çift tıklanır.
4. Tıklanan noktaların koordinatları kaydedilir.
5. Perspektif dönüşümü uygulanır.
6. Yeni görüntü ekranda gösterilir.

Bu çalışma ile OpenCV'de fare koordinatlarını kullanarak perspektif dönüşümü yapmayı öğrendim.