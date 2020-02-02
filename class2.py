class PersegiPanjang:
	'''
	Sebuah kelas yang memodelkan persegi panjang.
	Mempunyai dua atribut yaitu panjang dan lebar.
	Bisa menghitung luas dan keliling.
	Bisa juga menggambar persegi panjang sesuai atribut
	'''
	def __init__(self, panjang, lebar):
		self.panjang = panjang
		self.lebar = lebar
	
	def hitung_luas(self):
		return self.panjang * self.lebar
		
	def hitung_keliling(self):
		return (2*self.panjang) + (2*self.lebar)
		
	def gambar_persegi_panjang(self):
		for i in range(0, self.lebar):
			for j in range(0, self.panjang):
				print ('*'),
			print ("")

	def gambar_persegi_panjang_tanpa_isi(self):
		for i in range(0, self.lebar):
			if i > 0 and i < self.lebar-1:
				for j in range(0, self.panjang):
					if j > 0 and j < self.panjang-1:
						print ('-'),
					else:
						print ('*'),
			else:
				for j in range(0, self.panjang):
					print ('*'),
			
			print ("")

PersegiPanjangA = PersegiPanjang(20, 10)
print (PersegiPanjang.__doc__)
print (PersegiPanjang.__name__)
print (PersegiPanjang.__dict__)
print (PersegiPanjang.__module__)
print (PersegiPanjang.__bases__)
print (PersegiPanjangA.__doc__)
print (PersegiPanjangA.__dict__)
print (PersegiPanjangA.__module__)