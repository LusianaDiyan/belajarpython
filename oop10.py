class Hero:

	def __init__(self, name, health, armor):
		#self.__name = name
		self.name = name
		self.__health = health
		self.__armor = armor
		#self._info = "name {} : \n\thealth: {}".format(self.__name, self.__health)


	# def getHealth(self):
	# 	return self.__health

	@property
	def info(self):
		#return self._info
		return "name {} : \n\thealth: {}".format(self.name, self.__health)

	@property
	def armor(self):
		pass
	
	@armor.getter #nama method
	def armor(self):
		return self.__armor

	@armor.setter
	def armor(self, input):
		self.__armor = input

	@armor.deleter
	def armor(self):
		print('armor di delete')
		self.__armor = None


sniper = Hero('sniper',100,10)

print(sniper.info)

sniper.name = 'Luis'
print(sniper.info)
sniper.name = 'Luis'
print(sniper.info)

print('getter dan setter untuk __armor : ')
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)

print('delete armor')
del sniper.armor
print(sniper.__dict__)