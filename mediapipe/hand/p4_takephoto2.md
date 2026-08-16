# El Kontrollü Kamera Uygulaması (Hand Tracking Camera)

Bu proje, OpenCV ve cvzone kütüphaneleri kullanılarak el hareketleri ve parmak sayıları ile kamerayı kontrol etmeyi sağlar.

> **Not:** Bu çalışma, daha önce geliştirilen `p3_takephoto.py` kodunun mantıksal hatalardan arındırılmış, sistem durumu (açma/kapama) eklenmiş ve geliştirilmiş hali olan `p4_takephoto2.py` versiyonudur.

---

## 📌 Proje Gelişimi (p3_takephoto.py vs p4_takephoto2.py)

### Eski Sürüm (`p3_takephoto.py`)
- Sadece belirli parmak kombinasyonlarına sabit zamanlayıcılar atıyordu.
- Sistem açma/kapama kontrolü yoktu, el görüldüğü an otomatik tetikleniyordu.
- Fotoğraf isimleri rastgele sayılarla (`random.randint`) kaydediliyordu.

### Geliştirilmiş Sürüm (`p4_takephoto2.py`)
- **Açma / Kapama Kontrolü:** 5 parmak gösterilerek sistem **AKTİF** hale getirilir, yumruk yapılarak (0 parmak) sistem **DURDURULUR**.
- **Düzenli Fotoğraf Kaydı:** Fotoğraflar `foto_1.jpg`, `foto_2.jpg` şeklinde sırayla kaydedilir.
- **Modüler İşlevler:**
  - **1 Parmak:** Anında fotoğraf çeker.
  - **2 Parmak:** 5 saniyelik geri sayım ile fotoğraf çeker.
  - **3 Parmak:** 10 saniyelik geri sayım ile fotoğraf çeker.

---

## 🚀 Kurulum ve Çalıştırma

Gerekli kütüphaneleri yüklemek için terminalde şu komutu çalıştırın:

```bash
pip install opencv-python cvzone mediapipe