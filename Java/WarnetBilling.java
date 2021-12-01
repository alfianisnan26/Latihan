import java.util.Scanner;

class WarnetBilling{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Long pendapatan = 0L;
        for(int i = 0; i< 4; i++){
            System.out.print("\nNama\t: ");
            String nama = sc.next();
            System.out.print("PC\t: ");
            String pc = sc.next();
            System.out.print("Jam\t: ");
            int jam = sc.nextInt();
            Long harga = 0L;
            
            if(pc.equals("A")) harga = 6000L;
            else if(pc.equals("B")) harga = 10000L;
            else{
                System.err.println("\nPeringatan : Jenis PC Tidak ditemukan\n");
                continue;
            }
            pendapatan += (harga * jam);
        }
        System.out.println("Pendapatan Hari ini : " + format(pendapatan));
        sc.close();
    }

    public static String format(Long value) {
        String str = String.valueOf(value);
        StringBuilder sb = new StringBuilder(str);
        for(int i = 0; i < (str.length() - 1)/3 ; i++) sb.insert(sb.length() - ((3 * (i + 1)) + i), '.');
        return "Rp. " + sb.toString() + ",00";
    }
}