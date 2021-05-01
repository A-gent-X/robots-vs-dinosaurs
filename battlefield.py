from herd import Herd
from dinosaurs import Dinosaurs
from fleet import Fleet
from robots import Robots

robots = Robots()
fleet = Fleet()
dinosaurs = Dinosaurs()
herd = Herd()

class Battlefield:
    def __init__(self):
        self.herd = ""
        self.fleet = ""

    def gather_herd(self):
        self.herd = Herd
        if Dinosaurs in Herd == True:
            print(Dinosaurs, "plague the battlefield")

    def command_fleet(self):
        self.fleet = Fleet
        if Robots in Fleet == True:
            print(Robots, "storm the battlefield")

    def intro(self):
        self.intro = "All is fair in Love and War!\n"
        "This is a battle to the death and only the strongest will be left standing!\n"
        "Strategize and strike precise!\n"
        print(self.intro)











