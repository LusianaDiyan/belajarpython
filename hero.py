class Hero:

	def __init__(self,name):
		self.health_pool = [0, 100, 200, 300, 400, 500]
		self.attPower_pool = [0, 10, 20, 30, 40, 50]
		self.armor_pool = [0,1,2,3,4,5]
		self.__name = name
		self.__exp = 0
		self.__level = 0

	def show_info(self):
		print("{}\n\tlevel: {}\n\thealth: {}\n\tattPower: {}\n\tarmor: {}".format(
				self.__name,
				self.__level,
				self.__health,
				self.__attPower,
				self.armor
			)
		)

	@property
	def health_pool(self):
		pass

	@property
	def attPower_pool(self):
		pass

	@property
	def armor_pool(self):
		pass

	@property
	def levelUp(self):
		pass

	@property
	def gainExp(self):
		pass

	@health_pool.setter
	def health_pool(self,input):
		self.__health_pool = input

	@attPower_pool.setter
	def attPower_pool(self, input):
		self.__attPower_pool = input

	@armor_pool.setter
	def armor_pool(self,input):
		self.__armor_pool = input

	@gainExp.setter
	def gainExp(self, input):
		self.__exp += input
		if (self.__exp >= 100):
			self.levelUp = self.__exp//100
			self.__exp += 100

	@levelUp.setter
	def levelUp(self, input):
		self.__level += input
		self.__health = self.__health_pool(self.__level)
		self.__attPower = self.__attPower(self.__level)
		self.__armor_pool = self.armor_pool(self.__level)

class Hero_intelligent(Hero):
	
	def __init__(self, name):
		super().__init__(name)
		self.health_pool = [0, 100, 200, 300, 400, 500]
		self.attPower_pool = [0, 10, 20, 30, 40, 50]
		self.armor_pool = [0,0,5,1,1,5,2,2,5]
		self.levelUp = 1
		
class HeroString(Hero):
	
	def __init__(self, name):
		super().__init__(name)
		self.health_pool = [0, 100, 200, 300, 400, 500]
		self.attPower_pool = [0, 10, 20, 30, 40, 50]
		self.armor_pool = [0,2,4,6,8,10]
		self.levelUp = 1
	