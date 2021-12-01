import '11.dart';

/**
 * Mixins and With statements
 */

class a {
  int x = 0;
  int y = 1;
  void tampilkan() {
    print("$x--$y");
  }

  void hanyaX() => print(x);
  void hanyaY() => print(y);
  get nilaiX => x;
  get nilaiY => y;
}

class b with a {
  @override
  void tampilkan() {
    int a = nilaiX + nilaiY;
    super.tampilkan();
  }
}

void main() {
  b myB = b();
  myB.tampilkan();
}
