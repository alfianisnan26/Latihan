import '7.dart';

/**
 * Tipe Data
 * Ada tujuh jenis tipe data dalam dart yaitu :
 * (Satuan)
 * Numbers - diisi oleh angka-angka
 * Booleans - diisi oleh nilai kebenaran, Benar/Salah (true/false)
 * Strings - diisi oleh huruf, kata, kalimat
 * 
 * (Himpunan)
 * Lists - himpunan dari objek tertentu (atau tipe data lain) dengan identifikasi random
 * Maps - himpunan dari objek tertentu (atau tipe data lain) dengan identifikasi yang ditentukan
 * (Undefined)
 * Undefined - diisi oleh jenis khusus
 */

//Numbers
num num1 = 10;
num num2 = 20.3;

// define variable bernama : num1, berjenis num (angka), diisi oleh nilai 10

//Number dapat menyimpan nilai angka baik berupa integer, maupun double;
int angka1 = 5739;
int angka2 = 20;

//Integer dapat menyimpan data dalam bentuk bilangan bulat
double angka3 = 0.2738;
double angka4 = 10.0;
double angka5 = 5;
//Double dapat menyimpan data dalam bentuk bilangan pecahan dan juga bulat
//Notes : penggunaan memori int lebih kecil daripada double

//Booleans
bool kebenaran1 = true;
bool kebenaran2 = false;

//Strings
String huruf = "A";
String kata = "Aku";
String kalimat = "Aku adalah anak gembala";

//Lists
List<int> himpunanAngka = [1, 10, 100, 1000, 100, 10, 1];
Set<double> setHimpunanAngka = {1.1, 10.2, 100.3, 1.2, 1.1, 100.3};

//Maps
Map<int, bool> mapKebenaran = {1: true, 2: false, 3: false, 4: true};
Map<String, List<int>> mapList = {
  "togel": List<int>.of([1, 2, 3, 4, 5]),
  "sel": List<int>.of([3, 4, 7, 4, 2])
};

////Undefined
void kosong;
var variabel = "Hello";
final finaldata = variabel;
const konstanta = {1, 6, 4, 200};
/**
 * Konstanta dan final dapat dipindahkan kedalam variable
 * tapi variable tidak dapat dipindahkan kedalam konstanta
 * variabel dan konstanta dapat dipindahkan kedalam final
 * konstanta dan final harus memiliki nilai awal
 * nilai awal konstanta berupa nilai pasti
 * nilai awal final bisa berupa variabel atau konstanta lain
 * void harus tidak memiliki nilai
 */

/**
 * Assign, Access, Modify
 */
//Assign
void main() {
  // Himpunan ada 2 jenis
  // List/Set (Kumpulan data tanpa identitas)
  // List (data nya bisa berulang)
  List<int> himpAngka = [1, 2, 3, 4, 5, 10, 20, 38, 2, 4, 10, 2, 4];
  // Set (data tidak boleh berulang, harus unik)
  Set<String> himpKata = {
    'Alfi',
    'Alfian',
    'iki',
  };
  // Map (Kumpulan data dengan identitas)
  //  ..Key.. ..Val..
  Map<String, int> mapBuah = {"jagung": 20, "stroberi": 200, "anggur": 20};

  int isiJagung = mapBuah["stroberi"]!;

  print(isiJagung);
}
