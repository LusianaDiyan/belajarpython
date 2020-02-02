class PersegiPanjang:
	def __init__(self, p, l):
		self.panjang = p
		self.lebar = l

	def SetPanjang(self, p):
		self.panjang = p

	def GetPanjang(self):
		return self.panjang

	def SetLebar(self):
		self.lebar = l

	def GetLebar(self):
		return self.lebar

	def HitungKeliling(self):
		return 2 * self.lebar + 2 * self.panjang

	def HitungLuas(self):
		return self.panjang * self.lebar