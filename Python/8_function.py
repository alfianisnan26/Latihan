# Function merupakan metode untuk membungkus blok program
# secara garis besar Function akan membantu penyederhanaan penulisan panjang dan kompleks

# ibaratkan kita perlu membuat sebuah blok program untuk mengecek angka ganjil atau genap
# dan akan di lakukan terhadap beberapa angka pada posisi program yang berbeda
# untuk menulis blok tersebut kita tidak perlu melakukan copy-paste seluruh blok program
# jika blok program tersebut berada dalam fungsi, maka hanya cukup mengambil fungsinya saja

def cekAngkaGanjil(angka):
    if(angka % 2 == 0):
        print(angka, "adalah Genap")
    else:
        print(angka, "adalah Ganjil")
        
# penulisan fungsi di definisikan dengan menuliskan def
# untuk menunjukkan bahwa bagian tersebut menjadi gerbang blok program bagi sebuah fungsi
# setiap fungsi dapat memiliki atau tidak sama sekali atribut
# atribut adalah variabel input dari sebuah fungsi, contoh dari atribut yang ada pada fungsi
# angka ganjil di atas adalah "angka"
# sehingga, saat kita menulsi cekAngkaGanjil(10), maka nilai 10 akan di masukkan kedalam
# variabel angka untuk dibaca pada blok program fungsi cekAngkaGanjil tersebut.
# tandanya sebuah sintaks merupakan fungsi adalah terdapatnya tanda kurung setelah nama fungsi
# print() adalah salah satu contoh fungsi sederhana yang fungsinya dapat menampilkan data pada terminal.

cekAngkaGanjil(5)
cekAngkaGanjil(8)
cekAngkaGanjil(10)

# contoh di atas merupakan cara pemanggilan fungsi dengan sebuah input.
# sama seperti variabel, sebelum memanggil fungsi tersebut, fungsi terlebih dahulu harus di
# definisikan terlebih dahulu dengan def.

def namaSaya():
    print("Admin")
    
for i in range(10):
    namaSaya()
    
# Contoh pemanggilan fungsi tanpa atribut adalah seperti contoh di atas

def cekAngka(a, b):
    if(a > b):
        print(a, "lebih besar dari", b)
    elif(a < b):
        print(a, "lebih kecil dari", b)
    else:
        print(a,"sama dengan", b)

# di atas merupakan contoh fungsi dengan atribut lebih dari satu

cekAngka(3, 9)

# cara memasukkan input pada atribut fungsi di masukkan sesuai susunan
# posisi atribut tersebut saat di definisikan, sehingga nilai 3 akan masuk pada variabel a
# sementara nilai 9 akan masuk pada variabel b

cekAngka(b = 9, a = 3)

# untuk memasukkan nilai pada input atribut fungsi tanpa susunan yang besar dapat
# dilakukan seperti contoh di atas ini, yaitu dengan melakukan assignmen internal
# saat menulis atribut, dan posisi penulisannya bebas, asalkan memanggil nama atribut tersebut
# di dalam kurung sebuah input atribut fungsinya.

def pesan(nama, prefix = "Halo"):
    print(prefix +  ",", nama)
    
# di atas merupakan pembentukan input atribut dengan nilai default
# jika tanpa nilai default, maka seluruh input atribut harus memiliki nilai
# sementara jika atribut memiliki nilai default, maka tidak diwajibkan di isi (opsional)
# atau bisa juga di isi, dan akan mengganti nilai dari atribut variabel tersebut

pesan("Admin")
pesan(nama = "Admin2")
pesan("Admin3", "Hai")
pesan(prefix="Hola", nama="Admin4")

# di atas ini merupakan beberapa cara untuk memanggil fungsi dengan atribut default
# untuk baris 72, "Admin" akan masuk kedalam fungsi nama
# variabel prefix didalam fungsi pesan akan berisi bernilai default yaitu "Halo"
# karena pada saat memanggil fungsi pesan("Admin") tidak mengganti prefix
# contoh 73 sama seperti 72 hanya saja variabel nama diisi dengan cara pemanggilan variabel atribut nya
# karena ini lah fungsi yang memiliki nilai default tidak harus diisi semua

# contohnya adalah seperti print("Halo", sep="-", end=" ") dimana sep dan end
# merupakan contoh dari jenis atribut default
# sep memiliki nilai default " ", dan end memiliki nilai default "\n"

# contoh 74, dan 75 adalah memanggil fungsi dan juga mengganti variabel default yang telah ditulis
# sehingga "Admin3" akan masuk kedalam nama, kemudian "Hai" akan mengganti variabel atribut prefix
# pada 75 "Hola" akan masuk kedalam variabel prefix, sementara "Admin4" masuk kedalam variabel nama

hasil = pesan("Admin")
print(hasil)

# setiap function sebenarnya memiliki kembalian, atau disebut sebagai return,
# contohnya adalah pada fungsi pesan, hasilnya adalah None, karena tidak ada kembaliannya

# di bawah ini contoh cara untuk mengembalikan sebuah nilai dari fungsi

def pertambahan(a, b):
    hasil = a + b
    return hasil # sintaks return akan mengembalikan nilai untuk keluaran (output) fungsi

output = pertambahan(10, 5)
print(output) # 15 , dengan memasukkan kembaliannya terlebih dahulu kedalam variabel output

print(pertambahan(10, 5)) # 15 , dengan memasukkan kembaliannya langsung di masukkan kedalam input print

# contoh fungsi di atas adalah nilai 10 masuk kedalam variabel a, nilai 5 kedalam variabel b
# dalam fungsi pertambahan a + b sehingga 10 + 5 = 15 kemudian dimasukkan kedalam variabel hasil
# sehingga hasil = 15, kemudian di kembalikan (return) sebagai hasil kembalian dari fungsi pertambahan
# sehingga saat ditulis outpu = pertambahan(10, 5), nilai 15 yang tadinya berada pada hasil di dalam
# fungsi pertambahan, isinya akan dipindahkan kedalam variabel output, kemudian akan di panggil pada print.

def cekAngka(a):
    if(a > 0):
        return "Positif"
    elif(a < 0):
        return "Negatif"
    else:
        return "Nol"
    
print(cekAngka(6)) # Positif
print(cekAngka(-31)) # Negatif
print(cekAngka(0)) # Nol

# diatas merupakan contoh lain cara penulisan fungsi dengan return

def bagiSisa(a, b):
    if(b == 0):
        return None, None
    else:
        bagi = a / b
        sisa = a % b
        return bagi, sisa
    
bagi, sisa = bagiSisa(12, 7)
if(bagi == None or sisa == None):
    print("Tidak boleh Nol")
else:
    print("Bagi :", bagi)
    print("Sisa :", sisa)
    
# di atas merupakan cara untuk mengembalikan beberapa variabel dari fungsi
# kembalian ini di kembalikan pada rangkaian variabel disebut sebagai tuple.

# menjalankan program ini
# python 8_function.py
# ekspektasi hasil dari program ini :
# 5 adalah Ganjil
# 8 adalah Genap
# 10 adalah Genap
# Admin
# Admin
# Admin
# Admin
# Admin
# Admin
# Admin
# Admin
# Admin
# Admin
# 3 lebih kecil dari 9
# 3 lebih kecil dari 9
# Halo, Admin
# Halo, Admin2
# Hai, Admin3
# Hola, Admin4
# Halo, Admin
# None
# 15
# 15
# Positif
# Negatif
# Nol
# Bagi : 1.7142857142857142
# Sisa : 5