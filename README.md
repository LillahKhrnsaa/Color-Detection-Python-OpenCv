🎨 Color Detection using OpenCV & Python

Proyek ini mendeteksi warna dari gambar statis maupun secara real-time melalui webcam.
Program akan menampilkan nama warna dan nilai RGB-nya ketika pengguna mengklik pada area tertentu di gambar/video.

🧠 Teknologi yang Digunakan
Teknologi	Deskripsi
🐍 Python 3.10+	Bahasa pemrograman utama untuk membangun project ini.
🎥 OpenCV	Digunakan untuk membaca, menampilkan, dan memproses gambar serta video dari webcam.
📊 Pandas	Untuk membaca dan memproses dataset warna dari file colors.csv.
🔢 NumPy	Untuk manipulasi array dan perhitungan numerik RGB.
🗂️ CSV Dataset (colors.csv)	Berisi daftar warna beserta nilai RGB dan nama warnanya.
⚙️ Persiapan Awal

Sebelum menjalankan project ini, pastikan kamu sudah menginstal Python di perangkatmu.
Cek dengan:

python --version


Jika belum ada, unduh dari python.org
.

🚀 Cara Menjalankan Project
1️⃣ Clone atau Unduh Project

Clone repository ini atau ekstrak file zip project ke direktori yang kamu inginkan:

git clone https://github.com/username/color-detection.git
cd color-detection

2️⃣ Buat Virtual Environment (venv)
python -m venv .venv

3️⃣ Aktifkan Virtual Environment
🪟 Windows
.venv\Scripts\activate

🐧 Linux / macOS
source .venv/bin/activate


Jika environment aktif, kamu akan melihat prefix seperti ini di terminal:
(.venv) PS C:\Users\LENOVO\Documents\ColorDetection>

4️⃣ Install Dependencies

Pastikan file requirements.txt sudah ada di folder project, lalu jalankan:

pip install -r requirements.txt


Isi dari requirements.txt:

opencv-python
numpy
pandas

5️⃣ Jalankan Program
🔹 Mode 1 – Deteksi Warna dari Gambar

Pastikan file colors.csv dan gambar (misalnya colorpic.jpg) ada di folder yang sama.
Lalu jalankan:

python color_detection.py -i colorpic.jpg


💡 Klik sekali di area gambar untuk menampilkan nama warna & nilai RGB-nya.
Tekan ESC untuk keluar.

🔹 Mode 2 – Deteksi Warna Real-Time dari Webcam
python realtime.py


💡 Klik di area video untuk menampilkan warna dan nilai RGB-nya.
Tekan ESC untuk keluar.

📁 Struktur Folder
color-detection/
│
├── color_detection_image.py       # Deteksi warna dari gambar
├── color_detection_realtime.py    # Deteksi warna dari webcam
├── colors.csv                     # Dataset warna (RGB & nama)
├── requirements.txt               # Daftar dependensi
└── README.md                      # Dokumentasi project

🖼️ Contoh Output

Klik pada gambar atau video → tampilkan nama warna dan nilai RGB.

Teks otomatis menyesuaikan → jika latar belakang terang, teks menjadi hitam agar terbaca.

💡 Catatan

Pastikan file colors.csv berada di folder yang sama dengan script Python.

Kamu bisa menambah warna baru di file colors.csv untuk hasil lebih akurat.

Gunakan Python 3.10+ agar kompatibilitas library optimal.

👩‍💻 Author

Lillah Khairunisa
📧 lillahkhairunisa02@gmail.com

💻 github.com/LillahKhrnsaa
