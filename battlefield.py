from herd import Herd
from weapon import Dinosaurs
from fleet import Fleet
from robots import Robots
from weapon import Weapon

robots = Robots()
weapon = Weapon()
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

    battle_status = "A winner will stand after the war ends"
    battle_field = "Land robots and dinosaurs will fight on"
    while battle_status in battle_field:
        if Herd > Fleet == True:
            print("A robot self-destructs\n")
        elif Herd > Fleet == False:
            print("A dinosaur has fallen\n")
        elif Herd in battle_field > Fleet == True:
            print("Message to central base bring out the weapon a soldier has fallen\n")
        elif Robots.Weapon in battle_field > Dinosaurs.Herd == True:
            print("Robot solders obliterated the herd with their deadly weapon\n")
        elif Robots.Fleet.Weapon <= Dinosaurs.Herd:
            print("Dinosaurs are struggling to fend the lethal mechanized fleet\n")
        elif Robots.Fleet.Weapon > Dinosaurs.Herd:
            print("Another warrior has fallen in the herd\n")
        else:
            print("The dinosaur herd collapse from exhaustion\n"
                  "Robot Fleet were unstoppable with their destructive weapon\n")
