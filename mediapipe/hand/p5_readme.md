# Virtual Mouse 🖱️

Bu proje, kamera ve el hareketleri kullanılarak mouse kontrol etmeyi sağlar.

## Kullanılan Kütüphaneler

* OpenCV
* MediaPipe
* PyAutoGUI

## Özellikler

* İşaret parmağı ile mouse hareket ettirme
* Başparmak ve işaret parmağını birleştirerek sol tıklama
* Gerçek zamanlı el takibi
* `Q` tuşu ile çıkış

## Kurulum

Gerekli kütüphaneleri yükleyin:

```bash
pip install opencv-python mediapipe pyautogui
```

Programı çalıştırmak için:

```bash
python virtual_mouse.py
```

## Kullanım

☝️ İşaret parmağı → Mouse'u hareket ettirir.

🤏 Başparmak + işaret parmağı → Sol tık.

`Q` → Programdan çıkış.

---

**Not:** Bu proje yapay zeka desteği kullanılarak geliştirilmiştir.
