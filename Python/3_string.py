pesan = "Halo nama saya Admin"

# string (str) merupakan jenis data yang dapat berisi huruf, kata dan kalimat
# tanda bahwa data merupakan string dimana saat pendefinisiannya
# menggunakan tanda kutip dapat berupa kutip dua, atau kutip satu

# "Halo nama saya Admin" <- benar
# Halo nama saya admin   <- salah, akan dibaca sebagai variabel
# 'Halo nama saya Admin' <- benar
# 'Halo nama saya admin" <- salah, karena pembuka (') dan penutupnya (") berbeda
# "Kata si ibu : "jangan main di lapang" <- salah, karena kutip sebelum jangan seolah-olah menutup string
# "Kata si ibu : "jangan main di lapang"" <- salah, karena kutip di dalam string sejenis dengan bungkusnya
# 'Kata si ibu : "jangan main di lapang"' <- benar dan tepat,
# saat ada kutip dua di dalam string, baiknya menggunakan kutip satu sebagai pembungkusnya
# sebaliknya, saat kutip satu di dalam string, maka baiknya menggunakan kutip dua sebagai pembungkusnya

pesan = 'aku berkata "Rindu itu berat, kamu gak akan kuat", kemudian dia tersenyum'
print(pesan) # aku berkata "Rindu itu berat, kamu gak akan kuat", kemudian dia tersenyum

pesan = "hari ini hari Jum'at"
print(pesan) # hari ini hari Jum'at

# terdapat perintah khusus pada string, yang akan dibaca berbeda saat di print
# \n <- garis baru
# \t <- tab
# \r <- reset (kembali ke posisi awal)
# \\ <- menulis garis miring (backslash)
# \" <- menulis kutip dua (") di dalam bungkus kutip dua
# \' <- menulis kutip satu (') di dalam bungkus kutip satu

print('Halo nyonya,\nHari ini hari Jum\'at,\tSelamat bergabung')
# Halo nyonya,
# Hari ini hari Jum'at, Selamat bergabung

print("Hahahahaha\rHehe") # Hehehahaha

print(" ") # 
# diatas melakukan print spasi saja

print("\n")
# melakukan prin garis baru

a = 1234        # data angka sebagai angka (integer)
a = "1234"      # data angka sebagai kalimat (string)
a = str(1234)   # data angka yang diubah menjadi kalimat (string)
a = int("1234") # data kalimat yang di ubah menjadi angka (integer)

# pengubahan string kedalam angka (int atau float) hanya dapat dilakukan ketika di dalam
# string tersebut hanya ada angka

int("1234") #   benar
# int("12 34")  <- salah karena terdapat spasi
# int("Saya")   <- salah karena bukan angka
int("-183") #   benar, penulisan angka negatif
# int("38.91")  <- salah, karena seharusnya menggunakan floa
float("38.91")  # benar
# float("38,91")<- salah, desimal menggunakan titik

# kita dapat melakukan penggabungan pada jenis data string dengan menggunakan lambang tambah (+)
# penggabungan ini disebut dengan istilah concatenation atau concat

a = "Hari"
b = "ini"
c = "Jum'at"

print(a + b + c) # HariiniJum'at
# penggabungan ini tidak akan menyebabkan penambahan spasi otomatis

print(a + " " + b + " " + c) # Hari ini Jum'at

print(10 + 20) # 30
print("10" + "20") # 1020

# kita tidak dapat melakukan penggabungan data berbeda,
# contohnya adalah menggabungkan string dengan int
# "10" + 10 # akan menyebabkan error
# "10" + str(10) # benar, karena "10" merupakan angka sebagai string, dan str(10)
# adalah mengubah 10 sebagai string

angka = 123

print("Angka saya : " + str(angka)) # Angka saya : 123

pesan = pesan.upper()
print(pesan) # HARI INI HARI JUM'AT
# fungsi upper() dari string akan membuat string menjadi huruf besar semua

pesan = pesan.lower()
print(pesan) # hari ini hari jum'at
# fungsi lower() dari string akan membuat string menjadi huruf kecil semua

pesan = pesan.capitalize()
print(pesan) # Hari ini hari jum'at
# fungsi capitalize() adalah membuat huruf pertama dari kalimat menjadi huruf besar

panjangKarakter = pesan.__len__()
print(panjangKarakter) # 20
# fungsi __len__() adalah untuk menghitung jumlah karakter, termasuk spasi nya juga di hitung

print(len(pesan)) # 20
# fungsi len() juga dapat di tulis seperti contoh di atas.

# menjalankan program ini dengan cara
# python 3_string.py
# hasil yang diharapkan
# aku berkata "Rindu itu berat, kamu gak akan kuat", kemudian dia tersenyum
# hari ini hari Jum'at
# Halo nyonya,
# Hari ini hari Jum'at,   Selamat bergabung
# Hehehahaha
#
#
#
# HariiniJum'at
# Hari ini Jum'at
#
#
# HariiniJum'at
# Hari ini Jum'at
# 30
# 1020
# Angka saya : 123
# HARI INI HARI JUM'AT
# hari ini hari jum'at
# Hari ini hari jum'at
# 20
# 20