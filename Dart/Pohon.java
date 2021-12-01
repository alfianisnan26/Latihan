public class Pohon {
    //Field
    public int jumlahDaun = 0;
    public int kuatAkar = 0;
    public int panjangBatang = 0;
    private int jumlahBuah = 0;
    
    //Constructor
    Pohon(int jumlahDaunAwal) {
        jumlahDaun = jumlahDaunAwal;
    }
    
    //Method
    public void berbuah() {
        jumlahBuah++;
    }
    
    public void tumbuh() {
        kuatAkar += 5;
        panjangBatang += 10;
        jumlahDaun += 25;
    }
    
    public void gugur() {
        jumlahDaun -= 2;
    }

    public static void main(String[] args) {
        Pohon mangga = new Pohon(1000);
        Pohon jeruk = new Pohon(250);

        mangga.tumbuh();
        mangga.tumbuh();
        mangga.tumbuh();
        jeruk.gugur();
        jeruk.berbuah();

        System.out.println(mangga.kuatAkar);
        System.out.println(jeruk.jumlahDaun);
        System.out.println(jeruk.jumlahBuah);
    }
}
