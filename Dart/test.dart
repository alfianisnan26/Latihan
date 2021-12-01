class Pohon {
  //Field
  int jumlahDaun = 0;
  int kuatAkar = 0;
  int panjangBatang = 0;
  int jumlahBuah = 0;

  //Constructor
  Pohon({int jumlahDaunAwal = 0}) {
    jumlahDaun = jumlahDaunAwal;
  }

  //Method
  void berbuah() {
    jumlahBuah++;
  }

  void tumbuh() {
    kuatAkar += 5;
    panjangBatang += 10;
    jumlahDaun += 25;
  }

  void gugur() {
    jumlahDaun -= 2;
  }
}

main(List<String> args) {
  Pohon mangga = Pohon(jumlahDaunAwal: 1000);
  Pohon jeruk = Pohon(jumlahDaunAwal: 250);

  mangga.tumbuh();
  mangga.tumbuh();
  mangga.tumbuh();
  jeruk.gugur();
  jeruk.berbuah();

  print(mangga.kuatAkar);
  print(jeruk.jumlahDaun);
  print(jeruk.jumlahBuah);
}
