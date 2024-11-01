# -*- coding: utf-8 -*-
"""Tugas Implementasi Image Filtering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lHimYknl97zN5EMEvwrB3Wl6VOv3rfo0
"""

import numpy as np

# Inisialisasi kernel/filter H (Contoh kernel 3x3 untuk deteksi tepi)
H = np.array([[1, 1, 1],
              [1, 4, 1],
              [1, 1, 1]])

# Inisialisasi gambar input X (Contoh gambar 5x5)
X = np.array([[0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0],
              [0, 1, 1, 1, 0, 0],
              [0, 1, 1, 1, 0, 0],
              [0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]])

# Mendapatkan ukuran gambar dan kernel
tinggi_gambar, lebar_gambar = X.shape
tinggi_kernel, lebar_kernel = H.shape

# Inisialisasi gambar output Y dengan nilai nol
Y = np.zeros((tinggi_gambar - tinggi_kernel + 1, lebar_gambar - lebar_kernel + 1))

# Melakukan operasi konvolusi
for x in range(Y.shape[0]):
    for y in range(Y.shape[1]):
        # Perkalian elemen-wise dan penjumlahan
        Y[x, y] = np.sum(X[x:x+tinggi_kernel, y:y+lebar_kernel] * H)

# Menampilkan hasil
print("Gambar output Y:")
print(Y)