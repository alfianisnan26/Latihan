import '10.dart';

/**
 * Inheritance extends
 */

class Tumbuhan {
  final _tingkat = 1;
  var _deskripsi = "Ini Adalah Tumbuhan ";
  static int total = 0;
  int jumlahdaun = 0;
  Tumbuhan() {
    Tumbuhan.total++;
    print("Tumbuhan $_tingkat");
  }
  static get jumlahtotal => total;

  void tambahJumlahDaun() => jumlahdaun++;
  get jumlahDaun => jumlahdaun;
  set daun(jumlahdaun) => this.jumlahdaun = jumlahdaun;
  void gugurDaun() => jumlahdaun = 0;
}

class Monokotil extends Tumbuhan {
  final deskripsi = "Berbiji Satu";
  static int total = 0;
  Monokotil() {
    Monokotil.total++;
    super._deskripsi += "Monokotil";
    print("Monokotil");
  }
  static get jumlahtotal => total;
}

class Dikotil extends Tumbuhan {
  final deskripsi = "Berbiji Banyak";
  final jumlahBiji;
  int jumlahBuah = 0;
  static int total = 0;
  Dikotil(this.jumlahBiji) {
    Dikotil.total++;
    _deskripsi += "Dikotil";
    print("Membuat Dikotil");
  }
  static get jumlahtotal => total;
  void tambahBuah() => jumlahBuah++;
  void kurangBuah() => jumlahBuah--;
  get semuaBuah => jumlahBuah;
  void hapusBuah() => jumlahBuah = 0;
  set buah(jumlahBuah) => jumlahBuah;
}

class Paku extends Monokotil {
  static int total = 0;
  final jenis;
  Paku({this.jenis = "Pakis Haji"}) {
    Paku.total++;
    print(deskripsi + " " + jenis);
    daun = 100;
  }
  static get jumlahtotal => total;
}

class Rambutan extends Dikotil {
  static int total = 0;
  final jenis;
  final _pesanRahasia = "Rambutan ada rambutnya";
  Rambutan({this.jenis = "Rambutan Aceh"}) : super(2) {
    Rambutan.total++;
    print(_deskripsi + " " + jenis);
    daun = 200;
  }
  static get jumlahtotal => total;
  get pesanRahasia => _pesanRahasia;
}

class Manggis extends Dikotil {
  static int total = 0;
  final jenis;
  Manggis(this.jenis, {var jumlahBiji = 5}) : super(jumlahBiji) {
    Manggis.total++;
    print(super._deskripsi + " " + jenis);
    daun = 800;
  }
  static get jumlahtotal => total;
}

void main() {
  Manggis manggis = Manggis("Manis");
  manggis.tambahBuah();
  Rambutan rambutan = Rambutan();
  print(rambutan.deskripsi);
  Paku paku = Paku();
  print(paku.jumlahdaun);
  int jumlahManggis = Manggis.jumlahtotal;
  print(jumlahManggis);
  print(Dikotil.jumlahtotal);
  print(Tumbuhan.jumlahtotal);
}
