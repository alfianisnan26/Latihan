/**
 * Lokalisasi Variabel dalam fungsi
 */

var globalVariable;
const globalKonstanta = 12345;

void kearifanlokal1() {
  var lokalVariabel = globalKonstanta;
  const lokalKonstanta = 200;

  globalVariable = 200;

  print("Kearifian Lokal 1");
  print("var   : $lokalVariabel");
  print("const : $lokalKonstanta");
}

void kearifanlokal2() {
  var lokalVariabel = globalVariable;
  const lokalKonstanta = 140;
  print("Kearifian Lokal 2");
  print("var   : $lokalVariabel\nconst : $lokalKonstanta");
}

void main() {
  print(globalVariable);
  print(globalKonstanta);
  kearifanlokal1();
  kearifanlokal2();
}
