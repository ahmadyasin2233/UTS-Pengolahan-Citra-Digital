import cv2
import numpy as np
import matplotlib.pyplot as plt
import os




# Membaca gambar dari folder assets

image_path = "assets/gambar.jpg"

# Cek apakah file ada
if not os.path.exists(image_path):
    print("Gambar tidak ditemukan!")
    exit()

# Membaca gambar
img = cv2.imread(image_path)


# Konversi BGR ke RGB
# (agar warna tampil benar di matplotlib)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Konversi ke Grayscale

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Gaussian Blur
# Mengurangi noise sebelum edge detection

blur = cv2.GaussianBlur(gray, (3, 3), 0)


# Sobel X
# Deteksi tepi horizontal

sobel_x = cv2.Sobel(
    blur,
    cv2.CV_64F,
    1,
    0,
    ksize=3
)


# Sobel Y
# Deteksi tepi vertikal

sobel_y = cv2.Sobel(
    blur,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)


# Menghitung magnitude gradient

sobel = cv2.magnitude(sobel_x, sobel_y)


# Konversi ke uint8

sobel = np.uint8(np.absolute(sobel))


# Menyimpan hasil

output_folder = "hasil"

# Membuat folder jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cv2.imwrite(f"{output_folder}/grayscale.jpg", gray)
cv2.imwrite(f"{output_folder}/blur.jpg", blur)
cv2.imwrite(f"{output_folder}/sobel.jpg", sobel)

print("Hasil berhasil disimpan!")


# MENAMPILKAN HASIL


plt.figure(figsize=(15, 5))


# Original Image

plt.subplot(1, 4, 1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis("off")


# Grayscale

plt.subplot(1, 4, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")
plt.axis("off")


# Blur

plt.subplot(1, 4, 3)
plt.imshow(blur, cmap='gray')
plt.title("Gaussian Blur")
plt.axis("off")


# Sobel Edge Detection

plt.subplot(1, 4, 4)
plt.imshow(sobel, cmap='gray')
plt.title("Sobel Edge")
plt.axis("off")


# Menampilkan semua gambar

plt.tight_layout()
plt.show()