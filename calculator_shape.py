class Shape:
	def hitungLuas(self):
		pass

class PersegiPanjang(Shape):
	def __init__(self, panjang, lebar):
		self.panjang = panjang
		self.lebar = lebar

	def hitungLuas(self):
		return self.panjang * self.lebar

class Persegi(Shape):
	def __init__(self, sisi):
		self.sisi = sisi

	def hitungLuas(self):
		return self.sisi * self.sisi

class Segitiga(Shape):
	def __init__(self, alas, tinggi):
		self.alas = alas
		self.tinggi = tinggi

	def hitungLuas(self):
		return 0.5*self.alas*self.tinggi

b1 = PersegiPanjang(12,6)
b2 = Persegi(6)
b3 = Segitiga(4,8)
b4 = Segitiga(3,6)

class CalculateShape:
	totalLuas = 0
	def add(self, Shape):
		count = Shape.hitungLuas()
		CalculateShape.totalLuas += count

	def luasTotal(self):
		return CalculateShape.totalLuas

cs = CalculateShape()
cs.add(b1)
cs.add(b2)
cs.add(b3)
cs.add(b4)
print("Total Luas Bangun =",cs.luasTotal())		