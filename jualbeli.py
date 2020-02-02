class Buah:
	def __init__(self, name, hargaAwal, untung, tawar):
		self._name = name
		self._hargaAwal = hargaAwal
		self.untung = 0
		self.tawar = tawar
		self.laba = 0
		print("Harga beli " + name + " : ")

	def getHarga(self):
		return self._hargaAwal

	def setUntung(self, untung):
		self._hargaAwal += untung

	def setHargaTawar(self, tawar):
		print("Harga tawar : ", tawar)
		self._hargaAwal -= tawar

	def keuntungan(self):
		print("Keuntungan : {}".format(self._hargaAwal + self.untung - self.tawar))

	@property
	def untung(self):
		#return self.untung
		pass

	@untung.setter
	def untung(self, laba):
		self.untung = self._hargaAwal + laba

	@property
	def tawar(self):
		# return self.tawar
		pass
	
	@tawar.setter
	def tawar(self, tawar):
		self.tawar = tawar
		self.laba = self.tawar - self._hargaAwal

	def setUntung(self,inputUntung):
		self.untung = self.hargaBeli + inputUntung

	def setHargaTawar(self,inputHargaTawar):
		self.tawar = inputHargaTawar
		#menghitung untung
		self.keuntungan = self.hargaTawar - self._hargaAwal

mangga = Buah('Mangga', 5000, 0, 0)
print(mangga.getHarga())
mangga.setUntung(4000)
print("Harga jual Mangga : " )
print(mangga.getHarga())

mangga.setHargaTawar(7000)
mangga.keuntungan()


print("----------------------------------")
anggur = Buah('Anggur',30000, 0, 0)
anggur.untung=40000
anggur.tawar = 50000
print(anggur.getHarga())
print("Harga Jual Anggur : {}".format(anggur._hargaAwal + anggur.untung))
print("Harga tawar : {}".format(anggur.tawar))
anggur.keuntungan()
