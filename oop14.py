class Hero:
	def __init__(self, name, health):
		self.name = name
		self.health = health

class Hero_intelligent(Hero):
	def __init__(self,name):
		super().__init__(name,100)

class Hero_strength(Hero):
	def __init__(self,name):
		super().__init__(name,100)

lina = Hero_intelligent('lina')
axe = Hero_intelligent('axe')