from weapon import Weapon
from dinosaurs import Dinosaurs

dinosaurs = Dinosaurs()
weapon = Weapon()
weapon.weapon_armory()



class Robots:
    def __init__(self, name):
        self.name = name
        self.power_lvl = 25
        self.health = 100
        self.weapon = self.weapon('proton disintegrater, 50')

    def attack(self):
        dinosaurs.health -= self.weapon.attack_power
        dinosaurs.energy -= self.weapon.attack_power
