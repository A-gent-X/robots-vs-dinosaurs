from robots import Robots

class Dinosaurs:
    def __init__(self, dinosaur_type):
        self.attack_power = 20
        self.health = 120
        self.energy = 60
        self.dinosaur_type = dinosaur_type

    def attack(self):
        Robots.health -= self.attack_power()
        Robots.power_lvl -= self.attack_power()

    def attack_types(self):
        attack_type = ('guillotine bite', 'Horn thrust', 'Juggernaut charge')
        print(attack_type)
        if attack_type == attack_type is True:
            for attacks in attack_type:
                print(f"Dinosaur use {attack_type}")

