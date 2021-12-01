import 'dart:math';

/**
 * Operasi matematika
 */

int penjumlahan(int a, int b) => a + b;
int pengurangan(int a, int b) => a - b;
int perkalian(int a, int b) => a * b;
double pembagian(int a, int b) => a / b;
num perpangkatan(int a, int b) =>
    pow(a, b); //fungsi pow diambil dari library dart:math
num pangkatakar(int a) =>
    sqrt(a); //fungsi akar pangkat dua dari librarty dart:math
int increment(int a) {
  print(a++);
  print(++a);
  return a;
}

int decrement(int b) {
  print(b--);
  print(--b);
  return b;
}

List<num> operasiAssignment(num a, num b) {
  a = a + b; //explicit assigment
  a += b;
  a -= b;
  a *= b;
  a /= b;
  a++;
  --b;
  return List<num>.of([a, b]);
}

void main() {
  // akses fungsi dengan menyimpannya kedalam variabel
  //var hasilPembagian = pembagian(200, 2);
  //print(hasilPembagian);

  //print(penjumlahan(10, 20)); //akses fungsi secara langsung

  int a = 10;
  int b = 20;
//30  10  20
  a = a + b;
//50  30  20
  a = a + b;
//100 50  50
  a = a + a;

  a *= --b + a++; // a = a * (b + a)

  print(a);
}
