/**
 * Class untuk mendefinisikan objek
 */
class Pohon {
  //Field - merupakan variable global yang diakses oleh kelas tersebut
  //Normal Data merupakan data yang dapat diakses oleh kelas yang sudah dibuat
  String sambutan = "Halo Selamat datang di Pohon";

  var namaPohon;
  var jumlahDaun;
  var umurAsli;
  //Static Data merupakan data yang dapat diakses oleh kondisi apapun
  static String pohonese = "Ini adalah kelas pohon";
  static int jumlahPohon = 0;

  //Constructor adalah fungsi yang dipanggil saat membentuk objek dari kelas
  Pohon(this.namaPohon,
      {this.jumlahDaun = 1000, int umurPohon = 0, int kematian = 200}) {
    umurAsli = umurPohon + kematian;
    Pohon.jumlahPohon++;
  }

  void printData() {
    var umurAsli = 200;
    print("\nnama : $namaPohon");
    print("jd   : $jumlahDaun");
    print("ua   : ${this.umurAsli}");
    print("ual  : $umurAsli");
  }
}

void main() {
  Pohon rambutan = Pohon("Rambutan");
  Pohon mangga = Pohon("Mangga", kematian: 1200);

  print("${Pohon.pohonese}\nJumlah Total : ${Pohon.jumlahPohon}");

  rambutan.printData();
  mangga.printData();
}
