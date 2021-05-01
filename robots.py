from weapon import Weapon

class Robots:
    def __init__(self, name):
        self.name = name
        self.power_lvl = 25
        self.health = 100
        self.weapon = self.weapon('proton disintegrater, 50')

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power











