/**
 * If-Else Clause dan Logika
 * untuk melakukan pengujian data
 * hasil pengujian berupa boolean (true/false)
 * 
 * berikut operasi pengecekan data
 * == sama dengan
 * != tidak sama dengan
 * > lebih besar dari
 * >= lebih besar sama dengan
 * < lebih kecil dari
 * <= lebih kecil sama dengan
 * 
 * berikut operasi logika
 * || logika or
 * contoh :
 * && logika and
 * ! logika not negasi
 */

const Map<int, int> angka = {0: -20, 1: -10, 2: 0, 3: 10, 4: 20, 5: 10, 6: 0};
const kekosongan = null;

void main2() {
  print(angka);
  print(angka[3] == angka[5]); //10 == 10  : true
  print(angka[3] == angka[6]); //10 == 0   : false
  print(angka[3] != angka[5]); //10 != 10  : false
  print(angka[3] != angka[6]); //10 != 0   : true
  print(angka[3]! > angka[5]!); //10 > 10  : false
  print(angka[3]! > angka[6]!); //10 > 0   : true
  print(angka[3]! >= angka[5]!); //10 >= 10: true
  print(angka[5]! < angka[3]!); //10 > 10  : false
  print(angka[6]! < angka[3]!); //10 > 0   : true
  print(angka[5]! <= angka[3]!); //10 >= 10: true
  print(true && true); //true;
  print(true && false); //false;
  print(false && true); //false
  print(false && false); //false
  print(true || true); //true;
  print(true || false); //true;
  print(false || true); //true
  print(false || false); //false
  print(!true); //false
  print(!false); //true

  if (true) print("if ini true");
  if (false) print("if ini false");

  const cek = false;
  if (cek) {
    print("Masuk kedalam true");
  } else {
    print("Masuk kedalam false");
  }

  var angkaku = angka[4];
  if (angkaku! < 0) {
    print("angka negatif");
  } else if (angkaku == 0) {
    print("angka sama dengan nol");
  } else
    print("angka positif");
}

String pengecekanSimple(int angka) => (angka % 2 == 1) ? "ganjil" : "genap";

void main(List<String> args) => args.forEach(
    (element) => print("$element\t: ${pengecekanSimple(int.parse(element))}"));
