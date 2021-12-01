/**
 * Fungsi (Method)
 * Mempelajari cara membuat fungsi
 * Konsep sebuah fungsi adalah
 * input -> fungsi -> output
 * 
 * interpretasi fungsi pada matematika sederhana :
 * f(x, y) = x + y  : pendefinisian fungsi
 * c = f(x, y)      : penggunaan fungsi
 */

/**
 * Pendefinisian fungsi standar tanpa parameter input dan tanpa return output
 * void - jenis return dari fungsi
 * tampilkan - nama fungsi
 * () - parameter input (tanpa parameter)
 * => - menunjukkan fungsi dengan satu baris kode
 * print() - isi dari kode contoh
 * 
 * [tipe data return] [nama fungsi] () => [satu baris kode];
 */
void tampilkan() => print("print tampilkan");

/**
 * Pendefinisian fungsi standar dengan input tanpa return pada fungsi beberapa
 * baris kode
 * void - jenis return dari fungsi
 * tambah - nama fungsi
 * int a - nama input parameter (a) dengan jenis data inputnya b
 * int a, int b - menggunakan koma (,) untuk memisahkan beberapa input
 * () - input parameter
 * {} - blok kode dari fungsi beberapa baris kode
 * [tipe data return] [nama fungsi] ([parameter input]) {[blok kode]}
 */
void tambah(int a, int b) {
  var c = a + b;
  print(c);
}

/**
 * Pendefinisian fungsi dengan input wajib dan opsional tanpa return pada
 * beberapa baris kode
 * void - jenis data return
 * kurang - nama fungsi
 * () - input parameter wajib
 * ({}) - input parameter opsional (wajib memberikan nilai inisiasi)
 * int d - input wajib, tanpa inisiasi
 * int e = 10 - input opsional dengan inisiasi, jika tidak digunakan akan memiliki
 * nilai sama dengan inisiasi
 * {} - blok kode beberapa baris
 * [tipe data return] [nama fungs] ([fungsi wajib] {[fungsi opsional]}) {[blok kode]}
 */
void kurang(int d, {int e = 10}) {
  var f = d - e;
  print(f);
}

/**
 * Pendefinisian fungsi standar dengan return pada fungsi dengan satu baris kode
 * String - tipe data return berupa string
 * sambutan - nama fungsi
 * () - parameter input
 * String nama - input nama dengan jenis String
 * => - menunjukkan satu baris kode
 * "Hello " + nama - merupakan satu baris kode tersebut
 * fungsi akan mengembalikan nilai "Hello " + nama;
 * [tipe data return] [nama fungsi] ([parameter]) => [blok kode return];
 */
String sambutan(String nama) => "Hello " + nama;

/**
 * fungsi diatas relevan dengan fungsi berikut jika ditulis dalam bentuk multi-line
 * [tipe data return] [nama fungsi] ([parameter])
 * {
 *  [blok kode];
 *  return [return statement];
 * }
 */
String samButan(String nama) {
  return "Hello " + nama;
}

/**
 * Fungsi dengan return berupa jenis Get
 * [tipe data return] get [nama method] {
 * [blok kode];
 * return [return statement];
 * }
 */
String get maduRasa {
  String a = "IniMaduRasa";
  a += " RasaJeruk";
  return a;
}

/**
 * Fungsi set
 * set akan selalu void
 * set [nama method] => [blok program];
 */
set jumlahBuah(jumlah) => print(jumlah);

/**
 * Fungsi main standar adalah fungsi main tanpa input parameter :
 * void main(){}
 */
/**
 * Fungsi main dengan input parameter yang dapat diset saat melakukan compiling
 */
void main(List<String> input) {
  //print(input);
  //tampilkan();
  //tambah(10, 15);
  //kurang(20);
  //kurang(20, e: 200);
  //String hasil = sambutan("Alfian");
  //print(hasil);
  //print(samButan("Badrul"));
}

int perkalian(int a, int b) {
  return a * b;
}

void main2(List<String> args) {
  print(perkalian(7, 5));
}
