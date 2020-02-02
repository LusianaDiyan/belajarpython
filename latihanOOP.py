class Hero:
	def __init__(self,nama, health, attackPower, armorNumber):
		self.nama = nama
		self.health = health
		self.attackPower = attackPower
		self.armorNumber = armorNumber

	def serang(self, lawan):
		print(self.nama + 'menyerang' + lawan.nama)
		lawan.diserang(self, self.attackPower)

	def diserang(self, lawan, attackPower_lawan):
		print(self.nama + 'diserang' + lawan.nama)
		attack_diterima -= attackPower_lawan/self.armorNumber
		print('serangan terasa : ' + str(attack_diterima))
		self.health -= attack_diterima
		print('darah ' + self.nama + ' tersisa ' + str(self.health))

sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikimaru',100,5,10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
