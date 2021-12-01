# Looping merupakan sebuah cara untuk melakukan perulangan pada blok program
# setiap perulangan tersebut disebut sebagai iterasi
# terdapat dua jenis looping yaitu :
# while (saat)
# for (untuk)

# penulisan perulangan mirip seperti if statement (branching) dimana setiap
# blok program perulangan akan memiliki gerbang pengujian dan blok program

a = 0
while a < 10:
    a += 1
    print(a)
    
print("Selesai")

# contoh program di atas saat di jalankan adalah sebagai berikut :
# pendefinisian a = 0 pada baris 10
# a di cek pada gerbang while dengan kondisi a < 10;
# saat a = 0, a < 10 akan true, sehingga akan membaca blok program while
# yaitu pada baris 12, melakukan penambahan (increment) satu angka pada a
# kemudian pada baris 13 melakukan print a, saat ini karena a telah di increment,
# maka print(a) akan menghasilkan nilai 1
# karena blok ini merupakan blok looping, maka dari ini, program akan
# kembali lagi membaca ke posisi gerbang dari looping tersebut, yaitu
# pada baris 11 dengan data yang telah diubah sebelumnya, sehingga a = 1
# saat dilakukan pengecekkan a < 10 akan menghasilkan true, sehingga masuk
# kembali kedalam blok program dan membaca baris 12, 13
# dilakukan lagi penambahan satu angka sehingga menjadi a = 2
# dan seterusnya akan di lakukan iterasi sampai a menyentuh a = 9
# kemudian saat masuk akan di lakukan penambahan satu angka yaitu a = 10
# saat program kembali membaca kondisi while, saat ini karena a = 10
# maka a < 10 akan menghasilkan false, kemudian program akan langsung
# loncat pada baris 15, menyatakan bahwa print Selesai, hal ini terjadi
# seperti pada if yaitu jika kondisi false maka program akan di lewat (bypass).

while a > 0:
    a -= 1
    b = 0
    while b < 5:
        print(a, b)

# sama seperti branching, pada looping juga dapat mengimplementasikan nested
# atau beranak pinak, yaitu di dalam while terdapat while atau
# di dalam loop ada loop

# di bawah ini merupakan contoh looping yang digunakan untuk menampilkan garis
# bilangan angka genap di bawah 100

a = True
b = 0
while a:
    b += 2
    print(b)
    if(b < 100):
        pass
    else:
        a = False
    
# while juga dapat menerima input variabel dengan data berupa boolean.
# pada contoh di atas a = True, sehingga while akan di jalankan
# setiap perulangan akan melakukan penambahan dan menampilkan nilai pada variabel b
# ada bagian branching disini, dimana saat b < 100 dijalankan pass, sehingga
# program akan melakukan iterasi lagi, tetapi jika b >= 100, maka akan memiliki
# kondisi False pada gerbang if, menyebabkan a = False, kemudian saat
# dilakukan iterasi kembali, a akan menjadi False pada gerbang while,
# sehingga program keluar dari blok program while tersebut.

a = 0
while True:
    b += 2
    if(not b > 100):
        break
    
# dengan output yang sama, yaitu untuk menampilkan angka genap di bawah 100,
# program di atas menggunakan perintah break, untuk keluar dari looping
# break akan memaksakan keluar dari looping, walaupun pada gerbang while
# data tidak berubah sama sekali menjadi False

a = 0
while True:
    a += 1
    print("Awal")
    if(a % 2 == 0):
        print(a, "Genap")
        continue
    elif(a < 100):
        break
    else:
        print(a, "Ganjil")
    print("Muter")
    
# perintah selanjutnya adalah continue, yaitu melanjutkan iterasi looping
# pada kondisi saat membaca gerbang if pada baris 84, jika saat kondisi nya True
# maka akan di baca baris 85, dan 86.
# saat membaca 86, normalnya program akan keluar dari if, dan loncat untuk membaca
# bagian baris 91, karena menggunakan perintah continue,
# maka program akan langsung loncat kembali pada gerbang while pembuka nya sehingga
# akan kembali melakukan pembacaan kondisi pada baris 81.

