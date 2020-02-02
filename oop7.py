class Hero:
	jumlah = 0
	_privateJumlah = 0

	def __init__(self,name,health):
		self.name = name
		self.health = health

		self._private = "private"

		self._protected = "protected"

lina = Hero("lina",100)

print(lina.__dict__)
print(Hero.__dict__)
print(Hero._privateJumlah)