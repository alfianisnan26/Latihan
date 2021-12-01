import 'dart:io';

/**
 * IO Basics dan String
 */

void main() {
  const a = 100;
  const b = 200;
  const c = 300;
  const d = "Ini konstanta D";

  print("Standard Printer"); //standar printer untuk menampilkan String
  print(d); //printer konstanta atau variable lain
  print("Print " + a.toString()); //printer diikuti dengan variabel lain
  print("Print " + (a + b).toString()); //print dengan operasi dalam variabel
  print("Print $a"); //print data secara eksplisit
  print("Print $a$c"); //print beberapa data
  print("Print ${a + b}"); //print data dengan operasi

  //berlaku untuk memasukkan data kedalam string
  var input = stdin.readLineSync();
  print(input);
  var input2 = stdin.readLineSync();
  print(input! + input2!);
  print(int.parse(input) + int.parse(input2));

  print("Print1");
  print("Print2");
  stdout.write("Print1");
  stdout.write("Print2");
  print("\nLine1\nLine2");
  print("awalTab\t\t\takhirtab");

  print('Kutip Satu "AdaKutipDua" ');
  print("Kutip Dua 'AdaKutipSatu' ");

  print("printtanda spesial \' \" \$ ");

  String data1 = 'ini data 1';
  String data2 = 'ini data 2';
  String data3 = data1 + data2;
  print(data3);
}
