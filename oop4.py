class Hero:

	jumlah = 0

	def __init__(self, inputName, inputHealth, inputPower, inputArmor):
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		Hero.jumlah += 1
		print("membuat Hero dengan nama " + inputName)

	def siapa(self):
		print("namaku adalah " + self.name)

	def healthUp(self, up):
		self.health += up

	def getHealth(self):
		return self.health


hero1 = Hero("Snipper", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup",1000, 100, 0)
print(Hero.jumlah)

hero1.siapa()
hero2.healthUp(10)
print(hero1.getHealth())

# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)
# print(Hero.__dict__)