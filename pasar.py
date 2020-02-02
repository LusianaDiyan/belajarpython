class Buah:
	def __init__(self,inputNamaBuah,inputHargaBeli):
		self.namaBuah = inputNamaBuah
		self.hargaBeli = inputHargaBeli
		self.untung = 0
		self.hargaTawar1 = 0 
		self.keuntungan1 = 0
		self.hargaTawar2 = 0 
		self.keuntungan2 = 0

	@property
	def laba(self):
		pass
	
	@laba.setter
	def laba(self,inputUntung):
		self.untung = self.hargaBeli + inputUntung
	
	@property
	def tawar(self):
		pass
	
	@tawar.setter
	def tawar(self,inputHargaTawar):
		self.hargaTawar1 = inputHargaTawar
		self.hargaTawar2 = inputHargaTawar
		#menghitung untung
		self.keuntungan1 = self.hargaTawar1 - self.hargaBeli
		self.keuntungan2 = self.hargaTawar2 - self.hargaBeli
	
	def setUntung(self,inputUntung):
		self.untung = self.hargaBeli + inputUntung

	def setHargaTawar(self,inputHargaTawar):
		self.hargaTawar1 = inputHargaTawar
		self.hargaTawar2 = inputHargaTawar
		#menghitung untung
		self.keuntungan1 = self.hargaTawar1 - self.hargaBeli
		self.keuntungan2 = self.hargaTawar2 - self.hargaBeli
	
	def printNota(self):
		print("Harga Beli",self.namaBuah,self.hargaBeli)
		print("Harga Jual",self.namaBuah,self.untung)
		print("Harga Tawar",self.hargaTawar1)
		print("Harga Tawar",self.hargaTawar2)
		print("Laba Penjual",self.keuntungan1)
		print("Laba Penjual",self.keuntungan2)
		print("\n")

	def perbandingan(self):

		if self.hargaTawar1 > self.hargaTawar2:
			print("PEMBELI01 MEMPEROLEH BUAH\n")
		elif self.hargaTawar1 < self.hargaTawar2:
			print("PEMBELI02 MEMPEROLEH BUAH\n")
		else:
			print("Not sure\n")

print("BUAH MANGGA\n")
penjual = Buah("Mangga",15000)
penjual.printNota()
buah1 = Buah("Mangga",15000)
buah1.hargaTawar1 = 13000
buah1.hargaTawar2 = 10000
buah1.perbandingan()
#menggunakan method
print("---Perbandingan Harga Buah Mangga---")
mangga = Buah("Mangga (Pembeli01)",15000)
mangga.setUntung(4000)
mangga.setHargaTawar(13000)
mangga.printNota()

#menggunakan method
mangga = Buah("Mangga (Pembeli02)",15000)
mangga.setUntung(4000)
mangga.setHargaTawar(10000)
mangga.printNota()

print("<<<<---------------------------------->>>>")
print("BUAH ANGGUR\n")
penjual = Buah("Anggur",50000)
penjual.printNota()
buah2 = Buah("Anggur",15000)
buah2.hargaTawar1 = 45000
buah2.hargaTawar2 = 48000
buah2.perbandingan()

#menggunakan property
print("---Perbandingan Harga Buah Anggur---")
anggur = Buah("Anggur (Pembeli01)",50000)
anggur.laba = 40000
anggur.tawar = 45000
anggur.printNota()

#menggunakan property
anggur = Buah("Anggur (Pembeli02)",50000)
anggur.laba = 40000
anggur.tawar = 48000
anggur.printNota()	

