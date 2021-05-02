from robots import Robots


robots = Robots()

class Weapon:
    def __init__(self, weapon_type, attack_power):
        self.attack_power = attack_power
        self.weapon_type = weapon_type

    def weapon_armory(self):
        weapon_armory = ['Disintegration Ray', 'Plasma Saber', 'Graviton Cannon', 'Artic Polarity Shocker']
        print(weapon_armory)
        if weapon_armory in weapon_armory == True:
            for weapon_armory in weapon_armory:
                print(Robots, "chooses", weapon_armory)



