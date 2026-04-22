# 🖼️ Mini Image Editor — Peningkatan Kualitas Citra

### Menggunakan Brightness Adjustment & Upscale (Interpolation)

**Mata Kuliah:** Pengolahan Citra Digital
**Universitas Bina Sarana Informatika**

---

## 📦 Library yang Digunakan

| Library         | Kegunaan                        |
| --------------- | ------------------------------- |
| `streamlit`     | Membuat tampilan web interaktif |
| `opencv-python` | Pemrosesan citra (cv2)          |
| `numpy`         | Operasi matriks/array           |
| `Pillow`        | Membaca & menyimpan gambar      |

---

## 🚀 Cara Install & Menjalankan

### 1. Install Python

Pastikan Python versi 3.8 ke atas sudah terinstall:

```bash
python --version
```

Jika belum (Ubuntu):

```bash
sudo apt install python3 python3-pip python3-venv
```

---

### 2. Buat Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependency

```bash
pip install streamlit opencv-python numpy Pillow
```

atau:

```bash
pip install -r requirements.txt
```

---

### 4. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser:

```
http://localhost:8501
```

---

## 🖥️ Cara Menggunakan Aplikasi

1. **Upload gambar** (JPG/PNG) melalui sidebar
2. **Atur Brightness**

   * Nilai positif → gambar lebih terang
   * Nilai negatif → gambar lebih gelap
3. **Atur Kualitas (Upscale)**

   * Memperbesar resolusi gambar
   * Memberikan efek lebih halus / “HD”
4. **Lihat hasil**

   * Perbandingan gambar asli vs hasil edit
   * Statistik citra
5. **Download hasil** dalam format PNG atau JPG

---

## 📐 Metode yang Digunakan

### 1. Brightness Adjustment

Menambahkan nilai konstan ke setiap piksel:

```
x_baru = x + t
```

* `x` = nilai piksel (0–255)
* `t` = nilai brightness
* Hasil di-clip ke rentang 0–255

---

### 2. Upscale (Interpolation)

Memperbesar resolusi gambar menggunakan interpolasi bicubic:

* Ukuran gambar diperbesar (misal 2x, 3x, 4x)
* Piksel baru dihitung dari piksel sekitar
* Hasil terlihat lebih halus

📌 Catatan:
Upscale **tidak menambahkan detail baru**, hanya memperhalus tampilan.

---

## 📊 Fitur Aplikasi

* ✅ Upload gambar JPG/PNG
* ✅ Slider brightness interaktif
* ✅ Slider kualitas (Upscale / HD effect)
* ✅ Perbandingan citra sebelum & sesudah
* ✅ Statistik citra (mean, std, min, max)
* ✅ UI modern berbasis Streamlit
* ✅ Download hasil (PNG & JPG)

---

## 🗂️ Struktur Project

```
project/
│
├── app.py
├── requirements.txt
└── PANDUAN.md
```

---

## ❗ Troubleshooting

**Streamlit tidak ditemukan**

```bash
pip install streamlit
```

**OpenCV error**

```bash
pip install opencv-python
```

**Port sudah digunakan**

```bash
streamlit run app.py --server.port 8502
```

**Gambar tidak tampil**

* Pastikan format JPG atau PNG
* Hindari format seperti WEBP / HEIC

---

## 🎯 Catatan

Aplikasi ini merupakan pengembangan dari konsep dasar pengolahan citra menjadi **interactive image editor berbasis web**, dengan fokus pada peningkatan kualitas visual menggunakan:

* Brightness Adjustment
* Interpolation-based Upscaling

---

## 🚀 Pengembangan Selanjutnya

* 🔹 Before–After slider (seperti Photoshop)
* 🔹 Auto Enhance
* 🔹 AI Super Resolution (ESRGAN)

---
