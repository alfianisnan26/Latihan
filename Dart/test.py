class Pohon():
    # Field
    kuatAkar = 0
    panjangBatang = 0
    jumlahBuah = 0
    jumlahDaun = 0

    #Method
    def tumbuh(self):
        self.kuatAkar = self.kuatAkar + 5
        self.panjangBatang = self.panjangBatang + 10
        self.jumlahDaun = self.jumlahDaun + 25
    def berbuah(self):
        self.jumlahBuah = self.jumlahBuah + 1

mangga = Pohon()
mangga.tumbuh()
mangga.tumbuh()
mangga.tumbuh()
mangga.tumbuh()
print(mangga.jumlahDaun)