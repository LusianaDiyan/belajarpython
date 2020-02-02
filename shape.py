# class Segitiga():
# 	def __init__(self,alas,tinggi):
# 		self.alas = alas
# 		self.tinggi = tinggi
# 		self.luas = 0.5*alas*tinggi
# 	def hitungLuas(self):
# 		print("Luas Segitiga adalah ", self.luas)

# segitigaSamaKaki = Segitiga(10,10)
# segitigaSamaKaki.hitungLuas()

class Bentuk:
	def __init__(self):
		pass
	def hitungLuas(self):
		pass
	def hitungKeliling(self):
		pass
class Segiempat(Bentuk):
	def __init__(self, lebar):
		self.lebar = lebar
	def hitungLuas(self):
		return self.lebar * self.lebar
class PersegiPanjang(Segiempat):
	def __init__(self, panjang, lebar):
		super().__init__(lebar)
		self.panjang = panjang
	def hitungLuas(self):
		return super().hitungLuas()+(self.panjang-self.lebar)*self.lebar

bangun1 = Segiempat(10)
#print(bangun1.hitungLuas())
bangun2 = PersegiPanjang(20,10)
#print(bangun2.hitungLuas())
#bangun3 = PersegiPanjang(27.7,13.9)
#print(bangun3.hitungLuas())
bangun3 = PersegiPanjang(30,10)
# bangun4 = Segiempat(15)		
# bangun5 = Segiempat(20)
# bangun6 = Segiempat(20)
# daftarBangun = (bangun1,bangun2,bangun3,bangun4)
# daftarBangun2 = (bangun5,)
# listBangun = daftarBangun + daftarBangun2
# print(listBangun)
daftarBangun = []
daftarBangun.append(bangun1)
daftarBangun.append(bangun2)
daftarBangun.append(bangun3)

totalLuas = 0
for bangun in daftarBangun:
	totalLuas += bangun.hitungLuas()
print(totalLuas)
