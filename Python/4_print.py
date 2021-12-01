print("Helo world" + str(123))

# print merupakan fungsi sederhana untuk menampilkan data pada terminal

print("Halo") # melakukan print jenis data string
print(123) # melakukan print jenis data int
print(-283.12) # melakukan print jenis data float negatif
print(12 + (10.2 - 2)) # melakukan operasi aritmetika di dalam input print dapat dilakukan

a = 10
b = 20
print("Hasil perkalian : " + str(a * b)) # Hasil perkalian : 200
# melakukan print dengan menggabungkan string dan int yang diubah kedalam string

print(str(a) + " " + str(b)) # 10 20
# print di atas adalah melakukan penampilan isi data a dan b sekaligus menggunakan concat

print(a, b)
print("angka a :", a, "\nangka b :", b, "\nhasil perkalian", a * b)
# print di atas adalah melakukan penampilan isi data a dan b sekaligus menggunakan parameter print, sehingga
# dapat dipisahkan dengan koma dan otomatis menampilkan spasi di antara keduanya

print(a, b, sep=",") # 10,20
# print di atas adalah menampilkan a dan b dan dipisahkan dengan ,
# sep berfungsi untuk mengganti karakter pemisahnya, sehingga yang awalnya tanpa sep memiliki spasi
# di ganti menjadi koma

print("Aku", "Kamu", "Dia", sep="dan") # AkudanKamudanDia
print("Aku", "Kamu", "Dia", sep=" dan ") # Aku dan Kamu dan Dia

print(10, 20, sep=",", end=" || ")
print(30, 40, sep=",")

# 10,20 || 30,40
# end digunakan untuk mengganti karakter terakhir yang di print.
# secara default, print akan selalu menampilkan garis baru \n
# sehingga saat parameter end diganti, maka akan mengganti garis baru

# python 4_print.py
# Hasil ekspektasi dari program ini
# Helo world123
# Halo
# 123
# -283.12
# 20.2
# Hasil perkalian : 200
# 10 20
# 10 20
# angka a : 10
# angka b : 20
# hasil perkalian 200
# 10,20