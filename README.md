# 🎨 Color Detection using OpenCV & Python

Proyek ini bertujuan untuk **mendeteksi nama warna** dan **nilai RGB** dari gambar statis maupun secara real-time melalui *webcam*. Program akan menampilkan detail warna ketika pengguna mengklik pada area tertentu di gambar/video.

---

## 🧠 Teknologi yang Digunakan

| Teknologi | Deskripsi |
| :--- | :--- |
| 🐍 **Python 3.10+** | Bahasa pemrograman utama untuk membangun project ini. |
| 🎥 **OpenCV** | Digunakan untuk membaca, menampilkan, dan memproses gambar serta video dari webcam. |
| 📊 **Pandas** | Untuk membaca dan memproses dataset warna dari file `colors.csv`. |
| 🔢 **NumPy** | Untuk manipulasi array dan perhitungan numerik RGB. |
| 🗂️ **CSV Dataset (`colors.csv`)** | Berisi daftar warna beserta nilai RGB dan nama warnanya. |

---

## ⚙️ Persiapan Awal

Sebelum menjalankan project ini, pastikan kamu sudah menginstal **Python 3.10+** di perangkatmu. Cek dengan perintah:

```bash
python --version
````

Jika belum ada, unduh dari [python.org](https://www.python.org/downloads/).

-----

## 🚀 Cara Menjalankan Project

### 1️⃣ Clone atau Unduh Project

Clone repository ini atau ekstrak file zip project ke direktori yang kamu inginkan:

```bash
git clone [https://github.com/username/color-detection.git](https://github.com/username/color-detection.git)
cd color-detection
```

### 2️⃣ Buat Virtual Environment (venv)

```bash
python -m venv .venv
```

### 3️⃣ Aktifkan Virtual Environment

| Sistem Operasi | Perintah |
| :--- | :--- |
| 🪟 **Windows** | `.venv\Scripts\activate` |
| 🐧 **Linux / macOS** | `source .venv/bin/activate` |

Jika environment aktif, kamu akan melihat prefix `(.venv)` di terminalmu.

### 4️⃣ Install Dependencies

Pastikan file `requirements.txt` sudah ada di folder project. File ini berisi:

```
opencv-python
numpy
pandas
```

Lalu, jalankan perintah instalasi:

```bash
pip install -r requirements.txt
```

### 5️⃣ Jalankan Program

#### 🔹 Mode 1 – Deteksi Warna dari Gambar

Pastikan file `colors.csv` dan gambar target (misalnya `colorpic.jpg`) ada di folder yang sama.

```bash
python color_detection_image.py -i colorpic.jpg
```

> 💡 **Instruksi:** Klik sekali di area gambar untuk menampilkan nama warna & nilai RGB-nya. Tekan **`ESC`** untuk keluar.

#### 🔹 Mode 2 – Deteksi Warna Real-Time dari Webcam

```bash
python color_detection_realtime.py
```

> 💡 **Instruksi:** Klik di area video untuk menampilkan warna dan nilai RGB-nya. Tekan **`ESC`** untuk keluar.

-----

## 📁 Struktur Folder

```
color-detection/
│
├── color_detection_image.py    # Skrip deteksi warna dari gambar
├── color_detection_realtime.py # Skrip deteksi warna dari webcam
├── colors.csv                  # Dataset warna (RGB & nama)
├── requirements.txt            # Daftar dependensi
└── README.md                   # Dokumentasi project ini
```

-----

## 🖼️ Contoh Output

  - Klik pada gambar atau video → tampilkan nama warna dan nilai RGB.
  - Teks otomatis menyesuaikan → jika latar belakang terang, teks menjadi hitam agar terbaca.

> 💡 **Catatan Penting:**
>
> 1.  Pastikan file `colors.csv` berada di folder yang sama dengan script Python.
> 2.  Kamu bisa menambah warna baru di file `colors.csv` untuk hasil deteksi yang lebih akurat.
> 3.  Disarankan menggunakan **Python 3.10+** agar kompatibilitas library optimal.

-----

## 👩‍💻 Author

| Nama | Kontak |
| :--- | :--- |
| **Lillah Khairunisa** | 📧 `lillahkhairunisa02@gmail.com` |
| | 💻 [github.com/LillahKhrnsaa](https://www.google.com/search?q=https://github.com/LillahKhrnsaa) |

```
```
