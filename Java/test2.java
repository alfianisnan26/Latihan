import java.util.Scanner;

class test2 {
    public static void main(String[] args) {
        System.out.print("\nMasukkan nilai faktorial : "); //Memberi tahu user untuk memasukkan angka
        Scanner scanner = new Scanner(System.in); //Mendefinisikan objek scanner
        int faktorial = scanner.nextInt(); //Mengambil input berupa angka (integer)
        scanner.close(); //Menutup scanner
        int hasil = 1; //Mendefinisikan variabel hasil
        do{  //Melakukan looping minimal satu kali untuk memasukkan nilai pada variabel hasil
            System.out.printf("%d x ", faktorial); //Print nilai setiap angka anggota faktorial
            hasil *= faktorial--; //Menghitung faktorial dan mengurangi nilai faktorial setiap Looping
        }while(faktorial > 0); //Looping berjalan saat faktorial lebih dari nol
        System.out.printf("\b\b= %d\n\n", hasil); //Print hasil faktorial
    }
}