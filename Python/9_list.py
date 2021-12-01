# List merupakan kumpulan data. dalam matematika list ini merupakan implementasi dari
# bentuk kumpulan data yang terhimpun, disebut Himpunan.
# penulisan himpunan di tulis dengan kurung siku.
# biasanya isi dari himpunan (List) ini berjenis data sama.

himpunanAngka = [4,2,6,4,1,20]
himpunanNama = ["Adi", "Ferdi","Riski","Fernan", "Kevin"]

# di atas merupakan contoh himpunan
# cara memanggil seluruh himpunan, misalkan dalam print, kita dapat langsung memanggil
# nama dari himpunan tersebut

print(himpunanAngka) # [4, 2, 6, 4, 1, 20]

# untuk memanggil satu buah data pada himpunan dilakukan dengan menuliskan indeks
# di dalam kurung siku. Indeks dari himpungan di mulai dari nol,
# sehingga dapat di ilustrasikan sebagai berikut :
# ["Adi", "Ferdi","Riski","Fernan", "Kevin"]
#    0       1       2        3        4

print(himpunanNama[0]) # Adi
print(himpunanNama[2]) # Riski

# Jika kita memanggil himpunan dengan indeks di luar jenjangnya akan menghasilkan error
# contohnya adalah saat kita memanggil himpunanNama[5], akan eror, karena himpunanNama
# hanya memiliki indeks dari 0 sampai 4

# indeks yang dipanggil dapat menggunakan angka negatif, sehingga indeksnya mundur

# ["Adi", "Ferdi","Riski","Fernan", "Kevin"]
#   -5      -4      -3       -2        -1

print(himpunanNama[-3]) # Riski
print(himpunanNama[-1]) # Kevin

# kita juga dapat memanggil beberapa data List dalam range (jenjang) tertentu
# hasil dari pemanggilan list ini akan membentuk list baru.
# format pemanggilannya adalah himpunan[indeks_mulai:indeks_akhir]
# contohnya adalah kita ingin mengambil data indeks 2 sampai 3, maka :

print(himpunanNama[2:3]) # ["Riski", "Fernan"]

himpunanBaru = himpunanNama[2:3]
print(himpunanBaru[0]) # Riski
print(len(himpunanBaru)) # 2

# pemanggilan beberapa data himpunan juga dapat dipangil dari range paling awal untuk indeks_mulai
# dan paling akhir dari indeks_akhir

print(himpunanNama[:3]) # ["Adi", "Ferdi","Riski"]
print(himpunanNama[3:]) # ["Fernan", "Kevin"]

print("Panjang himpunan nama :", len(himpunanNama))
print("Panjang himpunan angka :", len(himpunanAngka))

# untuk mengetahui panjang himpunan (List) dapat menggunakan fungsi len, seperti pada len string

print(himpunanNama.__len__())

# fungsi __len__() dari himpunan juga dapat langsung di panggil dengan memberikan titik, kemudian
# memanggil fungsi __len__() di dalamnya.

# untuk menambahkan data pada List, kita dapat melakukannya dengan memanggil append()
# append() akan melakukan penambahan data di ujung list
# variabel_list.append(data_yang_akan_masuk)
# berikut merupakan contohnya

print(himpunanNama) # ["Adi", "Ferdi","Riski","Fernan", "Kevin"]
print(len(himpunanNama)) # 5

himpunanNama.append("Ahmad")

print(himpunanNama) # ["Adi", "Ferdi","Riski","Fernan", "Kevin", "Ahmad"]
print(len(himpunanNama)) # 6

# penambahan pada lokasi indeks spesifik dapat menggunakan fungsi insert
# dengan format penilusan sebagai berikut :
# variabel_list.insert(indeks_baru_yang_di_tambahkan, data_yang_di_tambahkan)

himpunanNama.insert(4, "Halo")

print(himpunanNama) # ['Adi', 'Ferdi', 'Riski', 'Fernan', 'Halo', 'Kevin', 'Ahmad']
print(len(himpunanNama)) # 7

# untuk menghapus data pada List dapat menggunakan fungsi internal remove()
# variabel_list.remove(data_yang_akan_di_hapus)

himpunanNama.remove("Adi")

print(himpunanNama) # ["Ferdi","Riski","Fernan", "Kevin", "Ahmad"]

himpunanNama.remove("Riski")

print(himpunanNama) # ["Ferdi","Fernan", "Kevin", "Ahmad"]

# untuk mengetahui keberadaan data pada sebuah List, kita
# dapat menggunakan in pada if statement

if "Riski" in himpunanNama:
    print("Ada")
else:
    print("Tidak")

# sebuah list juga dapat di lakukan perulangan iterasi menggunakan for loop
# contohnya adalah sebagai berikut :

for data in himpunanAngka:
    print(data, end=", ")
    
    
for data in himpunanAngka:
    if(data % 2 == 0):
        print(data, "adalah angka Genap")
    else:
        print(data, "adalah angka Ganjil")
        
        
# menjalankan program ini
# python 9_list.py

# hasil dari program ini
[4, 2, 6, 4, 1, 20]
# Adi
# Riski
# Riski
# Kevin
# ['Riski']
# Riski
# 1
# ['Adi', 'Ferdi', 'Riski']
# ['Fernan', 'Kevin']
# Panjang himpunan nama : 5
# Panjang himpunan angka : 6
# 5
# ['Adi', 'Ferdi', 'Riski', 'Fernan', 'Kevin']
# 5
# ['Adi', 'Ferdi', 'Riski', 'Fernan', 'Kevin', 'Ahmad']
# 6
# ['Adi', 'Ferdi', 'Riski', 'Fernan', 'Halo', 'Kevin', 'Ahmad']
# 7
# ['Ferdi', 'Riski', 'Fernan', 'Halo', 'Kevin', 'Ahmad']
# ['Ferdi', 'Fernan', 'Halo', 'Kevin', 'Ahmad']
# Tidak
# 4, 2, 6, 4, 1, 20, 4 adalah angka Genap
# 2 adalah angka Genap
# 6 adalah angka Genap
# 4 adalah angka Genap
# 1 adalah angka Ganjil
# 20 adalah angka Genap