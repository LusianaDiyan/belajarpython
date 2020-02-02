class Hero:

	#private class variable
	__jumlah = 0;

	def __init__(self, nama):
		self.__name = nama
		Hero.__jumlah += 1

	#method ini hanya berlaku untuk object
	def getJumlah(self):
		return Hero.__jumlah

	#method ini tidak berlaku untuk object
	def getJumlah():
		return Hero.__jumlah

	#method static (decorator) nempel ke object dan class
	@staticmethod
	def getJumlah2():
		return  Hero.__jumlah

	@classmethod
	def getJumlah3(cls):
		return cls.__jumlah

sniper = Hero('sniper')
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drowranger = Hero('drowranger')
print(Hero.getJumlah3())