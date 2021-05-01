class Dinosaurs:
    def __init__(self, dinosaur_type):
        self.energy_lvl = 20
        self.attack_power = 20
        self.health = 120
        self.dinosaur_type = dinosaur_type

    def attack(self):
        robot.health -= self.attack_power()