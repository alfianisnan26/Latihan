public class test{
   public static void main(String[] args) {
        //Bagian A
        boolean sedangHujan = true;
        if(sedangHujan){
            System.out.println("Bawa Payung");
        }

        //Bagian B
        boolean punyaPS5 = true;
        if(punyaPS5){
            System.out.println("Saya Bermain Game \"The Last of Us\"");
        }

        //Bagian C
        int uang = 10000;
        if(uang == 10000){
            System.out.println("Beli mie ayam");
        }

        //Bagian D
        String nama = "Udin";
        if(nama.equals("Daniel Craig")){
           nama = "James Bond";
        }
        System.out.println(nama);
        //hasil di print nya
        //Udin

        //Bagian E
        int uang_ = 100000;
        if(uang_ > 100000){
            int hari = 5;
            System.out.println("Bertahan Hidup di Sukabumi sebanyak " + hari  + " hari");
        }
    }
   
}