/**
 * Array
 */

const List<int> listArray = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, -1, -2];
const Set<int> setArray = {1, 2, 3, 4, 5};
const Map<int, String> mapArray = {
  1: "Andi",
  2: "Budi",
  3: "Rizki",
  4: "Sinta",
  5: "Udin"
};

void listMethod() {
  //Pengambilan data dari konstanta global
  var array = listArray;
  print(array[0]); //pengambilan data secara langsung : 1
  print(array
      .elementAt(0)); //pengambilan data dengan menggunakan method elementAt : 1
  print(array.length); //mengambil panjang dari data keseluruhan : 9
  print(array.isEmpty); //mengecek keberadaan isi array : false
  print(array.isNotEmpty); //mengecek keberadaan isi array : true
  print(array.indexOf(3)); //mengambil nomor index dari data yang dipilih : 2
  print(array.indexOf(
      3, 4)); //mengambil nomor index dimulai dari posisi tertentu : 6
  print(array.first); //mendapatkan data pertama
  print(array.last); //mendapatkan data terakhir
  //print(array
  //    .single); //mendapatkan element jika dalam array hanya memiliki tepat satu data
  array = array.reversed.toList(); //membalikan susunan data
  print(array);
  array.add(10); //menambahkan data pada array
  print(array);
  array.insert(3, -12); //menambahkan data pada posisi tertentu
  print(array);
  array.sort((a, b) => a.compareTo(b)); //menyusun posisi array
  print(array);
  array.remove(3); //Menghapus elemen sesuai objek input
  print(array);
  array.removeAt(0); //menghapus elemen pada lokasi index tertentu
  print(array);
  array.shuffle(); //mengacak data pada array
  print(array);
  var arraykecil = array.sublist(5); //mengambil sub-array
  var arraykecil2 = array.sublist(5, 7); //mengambil sub-array start-end
  var arraykecil3 =
      array.getRange(5, 7).toList(); //mengambil sub array dengan getRange
  print(arraykecil);
  print(arraykecil2);
  print(arraykecil3);
  print(array.contains(3)); //mengecek keberadaan element : true
  print(array.contains(-245)); //mengecek keberadaan element : false
  print(array.any((element) =>
      element > 10)); //mengecek keberadaan element dengan syarat tertentu
  print(array.every((element) =>
      element < 10)); //mengecek seluruh element berada pada syarat tertentu
  Set<int> iniSet = array.toSet(); //mengubah list menjadi set
  print(iniSet);
  Map<int, int> iniMap = array.asMap(); //Mengubahnya menjadi bentuk map
  print(iniMap);
  //mengoperasikan setiap data
  for (int a = 0; a < array.length; a++) {
    //menggunakan for loop
    print(array[a]);
  }
  for (var arr in array) {
    //menggunakan for-each loop
    print(arr);
  }
  array.forEach((element) {
    print(element);
  }); //menggunakan forEach pada array itu sendiri
  var dibawahNol = array
      .where((element) => element <= 0)
      .toList(); //mendapatkan sublist dengan syarat tertentu
  print(dibawahNol);
  List<double> iniDiMap =
      array.map((e) => e / 2).toList(); //mapping kedalam bentuk lain
  print(iniDiMap);
  print(iniDiMap.join());
  print(iniDiMap.join(", "));
  iniDiMap.clear(); //menghapus seluruh data;
  print(iniDiMap.isEmpty);
}

void setMethod() {
  print(setArray.length);
  print(setArray.first);
  print(setArray.isEmpty);
  print(setArray.isNotEmpty);
  print(setArray.last);
  //print(setArray.single);
  print(setArray);
  print(setArray
      .elementAt(2)); //Mendapatkan data set hanya melalui method elementAt
  var newSet = {1, 4, 6, 3, 9, 5};
  newSet = setArray.union(newSet);
  print(setArray.union(newSet));
  print(newSet.add(10)); //Menambahkan data jika data yang ditambahkan belum ada
  print(newSet);
  print(newSet.remove(10)); //menghapus data tertentu jika ada
  print(newSet);
  newSet.removeWhere((element) => element > 10); //menghapus data dengan syarat
  print(newSet);
  print(newSet.contains(10)); //mengecek keberadaan data
  print(newSet
      .any((element) => element < 10)); //mengecek keberadaan kondisi tertentu
  print(newSet.every((element) =>
      element < 10)); //mengecek seluruh data berada dalam kondisi tertentu
  print(newSet.join("-")); // mengubah kedalam String
  Set<double> iniDouble = newSet.map((e) => e.toDouble()).toSet();
  print(iniDouble);
  //dst
}

void mapMethod() {
  //dst
}

void main() {
  listMethod();
  setMethod();
}
