class Hero:
	def __init__(self, name,health, attackPower):
		self._name = name
		self._health = health
		self._attPower = attackPower

	#getter
	def getName(self):
		return self._name

	def getHealth(self):
		return self._health

	#setter
	def diserang(self, serangPower):
		self._health -= serangPower

	def setAttackPower(self,nilaibaru):
		self._attPower = nilaibaru

#awal dari game
earthshaker = Hero("earthshaker",50,5)

#game berjalan
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())
