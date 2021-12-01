# Python merupakan sebuah bahasa pemrograman
# <- lambang pagar di samping merupakan awal dari sebuah komentar
# komentar merupakan bagian program yang tidak "dibaca" oleh komputer
# sehingga bagian komentar dapat berisi apa saja, biasanya untuk memudahkan
# programmer untuk membaca dan memahami program

# dalam program terdapat input -> proses -> output
# terminal adalah bagian komputer untuk menjalankan aplikasi
# contoh terminal adalah cmd (Command Prompt)
# cmd dapat di jalankan dengan membuka start -> cmd

print("Hello World")

# bagian di atas merupakan salah satu contoh sintaks program python
# penulisan print harus ditulis seperti ini, yaitu ditulis dengan huruf kecil
# print merupakan fungsi, sehingga struktur penulisannya adalah print()
# kurung pada print digunakan sebagai tempat/wadah untuk menyimpan
# fungsi dari perintah print adalah untuk menampilkan data pada terminal.
# data yang akan di tampilkan sehingga print("Halo") akan menampilkan Halo
# print("Latihan") akan menampilkan latihan
# print(Tampilkan ini) akan error, karena Tampilkan ini tidak dibaca
# sebagai kalimat

ember = "Air"

# diatas merupakan contoh variabel dan proses "Assignment" yaitu memasukkan data
# kedalam variabel. ember merupakan nama dari variabel, yaitu sebagai wadah dari data
# sama dengan (=) merupakan proses untuk memasukkan data dari kanan (=) ke kiri (=)
# data yang dimasukkan kedalam ember adalah berjenis kalimat, sehingga data tersebut
# harus berada di dalam tanda kutip, boleh kutip satu (') atau kutip dua (") asalkan
# di buka dan ditutup oleh kutip yang sama jenisnya.
# "Baju" <- merupakan data berjenis kalimat (string) dengan isi Baju
# 'Kuda lumping' <- merupakan data berjenis kalimat (string) dengan isi Kuda lumping
# baju <- merupakan variabel bernama baju
# kuda lumping <- error, dikarenakan variabel tidak boleh memiliki pemisah (spasi)

# berikut ini cara penulisan variabel yang benar :

nama = "Kuda"
Nama = "Lumping"

# penulisan di atas adalah dengan memberi nama variabel nama dan Nama
# nama dan Nama merupakan variabel yang berbeda, walaupun di baca sama-sama nama
# tetapi karena N nya berbeda (kapital dan tidak), sehingga Nama dan nama merupakan
# variabel (wadah) yang berbeda

nama_saya = "Admin"
namaSaya = "Admin"

# penulisan variabel biasanya ditulis dalam huruf kecil semua, atau jika nama variabel
# merupakan gabungan beberapa kata, biasanya ditulis tanpa menggunakan spasi, tetapi dapat
# digabungkan dengan kaidah camelCase, dan snake_case

# nama_saya <- adalah bentuk penulisan snake_case atau tulisan ular, yaitu
# dengan menulis seluruh kata dengan huruf kecil smua yang setiap pemisah katanya dipisah
# dengan garis bawah (underscore)
# sekolah_menengah_atas_smandak

# namaSaya <- adalah bentuk penulisan camelCase atau tulisan unta, yaitu
# dengan menulis katanya dengan huruf kecil dan setiap kata baru selanjutnya menggunakan
# huruf kapital di awal huruf pada kata tersebut
# contoh :
# sekolahMenengahAtasSmandak

# berikut contoh penulisan variabel yang benar dan salah
# nama saya <- salah karena memiliki spasi
# nama!saya <- salah karena menggunakan karakter khusus
# 1namaSaya <- salah karena diawali angka
# asjj&*nk2 <- salah karena memiliki karakter khusus
# 1 <- salah, dibaca sebagai data berupa angka
# n <- benar
# i <- benar
# asjfdiasidjkasjsdUIOEp <- benar
# asjHHihjasiuiokHIH <- benar
# jumlahRumah <- benar
# jumlah_rumah <- benar
# _jumlahRumah <- benar
# __jumlah_rumah__ <- benar

# pemanggilan variabel pada print : 

print( ember) # Air
print ( nama ) # Kuda
print(nama_saya) # Admin

# ada spasi atau tidak di antara pemisah antara fungsi, lambang () dan variabel
# tidak akan memengaruhi program atau menyebabkan error

# cara memanggil variabel adalah seperti contoh diatas
# yaitu dengan memanggil variabel secara langsung dengan menuliskannya
# syarat variabel dapat dipanggil adalah harus di definisikan terlebih dahuli
# pendefinisian variabel ditandai dengan adanya proses assignemnt
# sebelum memanggil variabel ember, ember telah diisi terlebih dahulu di baris 24
# jika tidak dilakukan assignment terlebih dahulu, maka akan terjadi error
# karena variabel yang dipanggil tidak pernah diisi.

a = 10
b = 20

# proses diatas merupakan assignment membentuk variabel baru (mendefinisikan)
# yang diisi dengan isi baru

print(b) # 20

b = 30

print(b) # 30

# proses diatas merupakan assignemnt dengan mengganti data selanjutnya

b = a

# proses di atas merupakan assignment dengan mengganti data dari variabel lain
# definisi a = 10
# definisi b = 20
# penggantian b = a
# isi baru b = 10
# nilai a = 10 tetap tidak berubah.

x = a = b

# proses assignment dapat dilakukan beberapa kali dengan proses nya berjalan dari
# kanan ke kiri
# b mengisi a kemudian a mengisi x

print(x) # 10

# berkas program python disimpan dengan ekstensi .py seperti file ini yaitu 1_basic.py
# cara menjalankan file program python adalah dengan memanggil python
# melalui terminal atau cmd

# contoh :
# Asumsikan file 1_basic.py di simpan pada D:/latihan/python
# maka, pada cmd, ketikkan perintah berikut (windows) :
# python D:\latihan\python\1_basic.py

# untuk linux dan macos :
# python3 D:/latihan/python/1_basic.py

# hasil dari dijalankannya perintah tersebut adalah ditampilkannya :

# Hello World
# Air
# Kuda
# Admin
# 20
# 30
# 10