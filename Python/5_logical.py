# boolean (bool) merupakan jenis data logika
# data boolean hanya memiliki dua isi data, yaitu
# True <- artinya adalah benar
# False <- artinya adalah salah

# jenis data ini juga dapat di definisikan secara langsung dengan assignment

benar = True
salah = False

print(benar) # True
print(salah) # False

data = "True" # string berisi True
print(bool(data)) # string True dapat di ubah menjadi boolean

print(int(benar)) # True dapat di ubah kedalam angka menjadi 1
print(float(salah)) # False juga dapat diubah kedalam angka menjadi 0

# Perbandingkan logika dapat dilakukan untuk menguji dua data
# EQUALS atau sama dengan, merupakan proses perbandingan logika
# untuk mengetahui dua data memiliki nilai sama atau berbeda
# dapat digunakan untuk seluruh jenis data yang bersamaan yang memiliki isi data yang sama
# lambang sama dengan yang di pakai adalah == (dua sama dengan)
# pengujian ini harus menggunakan lambang ==, karena satu sama dengan (=)
# fungsinya telah digunakan sebagai proses assignment.

print(10 == 10) # True, karena 10 sama dengan 10
print(10 == 20) # False, karena 10 tidak sama dengan 20

a = 10
print(a == "10") # False, karena a sebagai int tidak sama dengan "10" sebagai string
print(a == int("10")) # True, karena "10" sudah di ubah menjadi int 

b = "Halo"
c = "halo"

print(b == c) # False, karena b memiliki H besar, sementara c memiliki h kecil
print(b.lower() == c) # True, karena b telah diubah menjadi huruf kecil semua
b = 10.0
print(a == b) # True, karena walaupun a dan b berbeda jenis, a=int, b=float. tetapi keduanya merupakan angka

# Perbandingan lainnya tersedia untuk angka, dapat digunakan untuk int dan float.
# yaitu lebih dari dan kurang dari
a = 10
b = 20

print(a > b) # False, a tidak lebih dari b
print(a < b) # True, a lebih dari b
print(a >= b) # False, a tidak lebih dari atau sama dengan b

b = 10
print(a <= b) # True, a sama dengan b

# penulisan lebih dari sama dengan dan kurang dari sama dengan
# ditulis lebih dari dan kurang darinya terlebih dahulu
# sehingga penulisan yang benar adalah sebagai berikut :
# a >= b | Benar
# a <= b | Benar
# a => b | Salah
# a =< b | Salah

# hasil dari logical juga dapat disimpan terlebih dahulu pada variabel
hasil = a % 2 > b
print(hasil) # False

# proses perbandingan logika juga dapat digabungkan dengan proses lain

hasil = ((a % 3) - 10 >= (b * 2)) == False
print(hasil) # True

# Operasi logika dilakukan untuk mengoperasikan data logika boolean (bool)
# terdapat tiga jenis operasi logik
# not   <- untuk melakukan negasi atau mengubah logika menjadi berkebalikan
# and   <- untuk memastikan seluruh data bernilai True
# or    <- untuk memastikan salah satu data bernilai True

print(not True, not False) # False, True
# not akan membalikkan data logika boolean, sehingga True akan berubah menjadi False,
# dan False akan berubah menjadi True

print(not not True) # True
# not dapat dirangkai sedemikian rupa sehingga data akan dapat dibalikkan lagi

print(not 10 == 20) # True mengecek data tidak sama dengan, sehingga jika data tidak sama, akan
# menghasilkan true

a = 10
b = 20
print(not (not a == b) == (not a < b)) # True

# operasi and (dan, mewajibkan seluruh data benar/True)
# adalah memastikan dua atau lebih data bernilai True semuanya
# jika seluruh data bernilai True, maka akan mengasilkan True
# jika salah satu data bernilai false, maka akan mengasilkan False

# Tabel kebenaran and adalah sebagai berikut
# T and T = T
# T and F = F
# F and T = F
# F and F = F
# T=True, F=False

print(True and True and False) # False
print(True and True) # True
print(False and True and True and True and True) # Sepanjang apapun True nya,
# maka jika terdapat False hasilnya
# pasti akan bernilai False

print(not(a % 2 == 0 and b % 2 == 0)) # False

# operasi or (atau, mengecek apakah salah satunya bernilai benar/True)
# adalah operasi logika yang akan menghasilkan True saat salah satu datanya bernilai True
# operasi ini akan menghasilkan False hanya saat seluruh data nya bernilai False

# Tabel kebenaran or adalah sebagai berikut
# T or T = T
# T or F = T
# F or T = T
# F or F = F
# T=True, F=False

print(True or True or False or False) # True
print(False or False) # False
print(a < b or a > b) # True

print(not a > b or (a < b and a == b)) # True

# Operasi logika dapat menggunakan distribusi atau kurung sebagai indikasi prioritas
# pengerjaan terlebih dahulu

a = 10
b = 20

print(a == b or a < b and False) # False

# pembacaan proses logika tanpa kurung dibaca dari kiri ke kanan sehingga,
# a == b or a < b and False
# a == b terlebih dahulu, menghasilkan False
# (a == b) or (a < b)
# False or True menghasilkan True
# ((a == b) or (a < b)) and False
# (True) and False mengasilkan False

# python 5_logical.py
# Hasil yang di harapkan
# True
# False
# True
# 1
# 0.0
# False
# False
# True
# False
# True
# True
# False