# salah satu jenis data pada bahasa python adalah number atau angka
# terdapat dua jenis data angka, yaitu :
# integer (int) -> bilangan bulat
# float (float) -> bilangan desimal

bilanganBulat = 10

# penulisan bilangan bulat ditandai dengan tidak memiliki koma

bilanganDesimal = 5.6

# penulisan bilangan desimal ditandai dengan adanya koma, yang ditulis dengan point (titik)
# jika bilanganDesimal = 5,6 yaitu ditulis dengan koma, hal ini tidak akan error,
# tetapi data bukan dibaca sebagai float, melainkan menjadi tuple (di jelaskan nanti)

# operasi aritmetika dapat dilakukan pada program python
# terdapat beberapa operasi matematika yang dapat langsung digunakan oleh programmer
# yaitu :
# +  <- penambahan
# -  <- pengurangan
# *  <- perkalian
# /  <- pembagian
# %  <- modulo (sisa bagi)
# ** <- pangkat

# berikut ini contoh sintaks program untuk melakukan operasi aritmetika

a = 10 * 20 # melakukan perkalian 10 * 20 kemudian hasil disimpan pada variabel a

b = 5
c = 2
d = b ** c # melakukan perpangkatan variabel b yang berisi 5, dan c berisi 2

a = (2 * b) + (3 * c)
a = b * 2 + ((10 - 2) * 20 + (-3))
# penulisan dapat menggunakan distribusi sesuai dengan kaidah matematika

angkaNegatif = -12.3
# penulisan negatif seperti menulis di ilmu matematika, yaitu dengan menambahkan lambang negatif

print(angkaNegatif - a) # -179.3
print((a % 2) - b) #-4

# proses aritmetika juga dapat langsung dilakukan di dalam wadah fungsi (sebagai parameter)

x = 10
y = 20
xy = x/y

print(xy) # hasil dari pembagian akan selalu berubah menjadi float

# proses yang dilakukan antara integer dengan integer akan menghasilkan integer
# proses yang dilakukan antara integer dengan float akan menghasilkan float
# proses yang dilakukan antara float dengan float akan menghasilkan float

x = 10.0 # variabel x bernilai 10.0 sebagai float
y = 10   # variabel y bernilai 10 sebagai integer

print(int(x)) # mengubah jenis data menjadi integer sehingga x dengan isi 10.0 di print menjadi 10

y = float(y) # mengubah jenis data y menjadi float yang awalnya merupakan integer
print(y)

a = 10
b = 20

a += b

# operasi di atas merupakan cara untuk melakukan operasi dengan dirinya sendiri
# sehingga a += b sama saja seperti menulis a = a + b

a *= b
print(a) # 600
a -= b
print(a) # 580
a /= b
print(a) # 29.0
a %= b
print(a) # 9.0
a **= b 
print(a) # 1.2157665459056929e+19

# print(a) akan berubah ubah karena variabel a datanya berganti saat dilakukan operasi tersebut

a = 0
print(a) # 0
a += 1
print(a) # 1
a -= 1
print(a) # 0

# a += 1 biasanya dikenal sebagai istilah "increment" yaitu melakukan penambahan satu nilai kedalam variabel
# sehingga yang awalnya 0, menjadi 1

# a -= 1 biasanya dikenal sebagai istilah "decrement" yaitu melakukan pengurangan satu nilai kedalam variabel
# sehingga yang awalnya 1, menjadi 0

# menjalankan program ini
# python 2_number.py

# hasil yang diharapkan
# -179.3
# -4
# 0.5
# 10
# 10.0
# 600
# 580
# 29.0
# 9.0
# 1.2157665459056929e+19
# 0
# 1
# 0