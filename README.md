# Pengolahan Citra Digital
# Implementasi Deteksi Tepi Menggunakan Metode Sobel

## Tentang Project

Project ini dibuat sebagai bagian dari tugas mata kuliah Pengolahan Citra Digital.

Fokus utama project ini adalah mengimplementasikan metode deteksi tepi menggunakan Sobel Operator untuk mendeteksi batas objek pada citra digital.

Metode Sobel digunakan untuk menampilkan perubahan intensitas piksel sehingga tepi objek pada gambar dapat terlihat lebih jelas.

---

# Tujuan

- Memahami konsep dasar deteksi tepi pada citra digital
- Mengimplementasikan metode Sobel menggunakan Python
- Mengidentifikasi bentuk dan batas objek pada gambar
- Membandingkan hasil citra sebelum dan sesudah proses deteksi tepi

---

# Landasan Teori

## 1. Citra Digital

Citra digital merupakan representasi gambar dalam bentuk data numerik yang terdiri dari kumpulan piksel.

Setiap piksel memiliki nilai intensitas tertentu yang dapat diproses menggunakan komputer.

---

## 2. Deteksi Tepi

Deteksi tepi adalah proses untuk menemukan perubahan intensitas yang signifikan pada suatu citra.

Tujuan utama deteksi tepi:
- mengenali bentuk objek
- mempermudah segmentasi citra
- membantu analisis visual

---

## 3. Metode Sobel

Sobel Operator adalah metode deteksi tepi yang bekerja dengan menghitung gradien perubahan intensitas pada arah horizontal dan vertikal.

Kernel Sobel Horizontal (Gx):

```text
-1 0 1
-2 0 2
-1 0 1
```

Kernel Sobel Vertikal (Gy):

```text
-1 -2 -1
 0  0  0
 1  2  1
```

Hasil akhir diperoleh dari kombinasi gradien horizontal dan vertikal.

---

# Kelebihan dan Kekurangan

## Kelebihan

- Implementasi sederhana
- Proses komputasi cepat
- Mampu mendeteksi tepi objek dengan cukup baik

## Kekurangan

- Sensitif terhadap noise
- Hasil tepi terkadang kurang halus

---

# Tools yang Digunakan

- Python
- OpenCV
- NumPy
- Matplotlib

---

# Instalasi

Install seluruh library yang dibutuhkan menggunakan perintah berikut:

```bash
pip install opencv-python numpy matplotlib
```

---

# Struktur Folder

```text
project/
│
├── assets/
│   └── gambar.jpg
│
├── hasil/
│   ├── grayscale.jpg
│   ├── blur.jpg
│   └── sobel.jpg
│
└── main.py
```

---

# Alur Program

1. Membaca citra dari folder assets
2. Mengubah citra menjadi grayscale
3. Mengurangi noise menggunakan Gaussian Blur
4. Mendeteksi tepi menggunakan Sobel Operator
5. Menyimpan hasil proses
6. Menampilkan hasil menggunakan matplotlib

---

# Cara Menjalankan Program

Jalankan file Python menggunakan perintah:

```bash
python main.py
```

---

# Hasil

| Original | Grayscale | Blur | Sobel Edge |
|---|---|---|---|
| Gambar asli | Citra grayscale | Hasil blur | Hasil deteksi tepi |

---

# Analisis

- Metode Sobel berhasil mendeteksi tepi objek pada citra
- Perubahan intensitas piksel dapat dikenali dengan baik
- Bentuk objek menjadi lebih jelas dibanding citra asli
- Gaussian Blur membantu mengurangi noise sebelum proses deteksi tepi

---

# Kesimpulan

Deteksi tepi citra dapat dilakukan menggunakan metode Sobel Operator.

Kesimpulan dari project ini:
- Sobel efektif untuk mendeteksi tepi objek
- Implementasi relatif mudah dilakukan
- Cocok digunakan untuk proses dasar pengolahan citra digital

---

# Penutup

Terima kasih telah melihat project ini.

Semoga project ini dapat membantu dalam memahami konsep dasar deteksi tepi pada pengolahan citra digital dan menjadi dasar untuk pembelajaran lebih lanjut.