import cv2
import numpy as np
import pandas as pd
import argparse

# Argument parser untuk input path gambar
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Path gambar")
args = vars(ap.parse_args())
img_path = args['image']

# Membaca gambar dengan OpenCV
img = cv2.imread(img_path)

if img is None:
    print("❌ Gambar tidak ditemukan. Periksa path-nya dengan benar.")
    exit()

# Global variables
clicked = False
r = g = b = xpos = ypos = 0

# Membaca file CSV warna
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# Fungsi untuk mencari nama warna terdekat
def getColorName(R, G, B):
    minimum = float('inf')
    cname = ""
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Fungsi untuk menangkap klik mouse
def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDOWN:  # klik tunggal agar lebih responsif
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# Inisialisasi window
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    frame = img.copy()  # buat salinan agar gambar asli tidak rusak

    if clicked:
        # Buat kotak warna di pojok atas
        cv2.rectangle(frame, (20, 20), (750, 60), (b, g, r), -1)

        # Tulis nama warna dan nilai RGB
        text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # Ubah warna teks jika warna terlalu terang
        if r + g + b >= 600:
            cv2.putText(frame, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    # Tampilkan frame
    cv2.imshow("image", frame)

    # Tekan ESC untuk keluar
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
