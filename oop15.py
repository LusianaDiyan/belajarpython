
from hero import Hero_intelligent, HeroString

lina = Hero_intelligent('lina')
slardar = HeroString('slardar')

lina.show_info()
slardar.show_info()

lina.gainExp = 200
slardar.gainExp = 250

lina.show_info()
slardar.show_info()
	