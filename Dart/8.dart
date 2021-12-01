/**
 * Looping (Iterasis)
 */

List<String> array = ["Andi", "Budi", "Adul", "Sinta", "Rizki"];

void main(List<String> args) {
  if (args.isEmpty) {
    print("Tak Kenal maka tak sayang");
  } else if (args[0] == "while") {
    print("While Loop");
    whileLoop();
  } else if (args[0] == "dowhile") {
    print("Do-While Loop");
    doWhileLoop();
  } else if (args[0] == "for") {
    print("For Loop");
    forLoop();
  } else if (args[0] == "foreach") {
    print("For Each Loop");
    forEachLoop();
  } else
    print("Tak Kenal maka tak sayang");
}

void whileLoop() {
  int a = 0;
  while (a < 10) {
    print("Nilai A ke = " + a.toString());
    a++;
  }
}

void doWhileLoop() {
  int a = 0;
  do {
    print("Nilai A ke = " + a.toString());
    a++;
  } while (a < 10);
}

void forLoop() {
  for (int a = 0; a < array.length; a++)
    print("Nilai ke = " + a.toString() + " adalah : " + array[a]);
}

void forEachLoop() {
  for (var arr in array) {
    print("Isi Array : $arr");
  }
}
