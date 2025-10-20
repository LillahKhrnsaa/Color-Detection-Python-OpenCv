import cv2
import pandas as pd

# Load color data
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("colors.csv", names=index, header=None)

# Global variables
clicked = False
r = g = b = xpos = ypos = 0

# Fungsi untuk mencari nama warna yang paling mendekati
def getColorName(R, G, B):
    minimum = float('inf')
    cname = ""
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Fungsi mouse event
def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos = x
        ypos = y
        b, g, r = frame[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# Buka webcam
cap = cv2.VideoCapture(0)  # 0 adalah kamera default
cv2.namedWindow('Webcam Color Detector')
cv2.setMouseCallback('Webcam Color Detector', draw_function)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if clicked:
        # Buat kotak warna di pojok atas
        cv2.rectangle(frame, (20, 20), (600, 60), (b, g, r), -1)

        text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # Ubah warna teks jika latar terlalu terang
        if r + g + b >= 600:
            cv2.putText(frame, text, (30, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, text, (30, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Webcam Color Detector", frame)

    # Tekan ESC untuk keluar
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Bersihkan
cap.release()
cv2.destroyAllWindows()
