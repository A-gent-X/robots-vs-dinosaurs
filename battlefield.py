# from herd import Herd
# from dinosaurs import Dinosaurs
# from fleet import Fleet
# from robots import Robots
# from weapon import Weapon
#
# robots = Robots()
# weapon = Weapon()
# fleet = Fleet()
# dinosaurs = Dinosaurs()
# herd = Herd()

class Battlefield:
    def __init__(self):
        self.herd = ""
        self.fleet = ""

    def gather_herd(self):
        Herd = "shake the battlefield with a mighty herd!"
        Dinosaurs = "Dinosaurs"
        # if Dinosaurs in Herd == True:
        print(Dinosaurs, Herd)
#
    def command_fleet(self):
        Fleet = ""
        Robots = input("\nRobots with foreign weapons...\n"
                       "\nStorm the battlefield with a large mechanized fleet!\n")
        # for Robots in Fleet:
        print(Robots)

    def run_intro(self):
        self.intro = ""
        print("\nAll is fair in Love and War!\n",
        "\nThis is a battle to the death and only the strongest will be left standing!\n"
        "\nStrategize and strike precise!\n")

    def run_battle_stimulation(self):
        Herd = ""
        Fleet = ""
        Weapon = ""
        battle_status = "A winner will stand after the war ends"
        battle_field = "Land robots and dinosaurs will fight on"
        while battle_status in battle_field:
            if Herd > Fleet:
                print("\nA robot self-destructs\n")
                break
            elif Herd > Fleet == False:
                print("\nA dinosaur has fallen\n")
            elif Herd > Fleet == True:
                print("\nMessage to central base bring out the weapon a soldier has fallen\n")
            elif Fleet.Weapon > Herd == True:
                print("\nRobot solders obliterated the herd with their deadly weapon\n")
            elif Fleet.Weapon >= Herd:
                print("\nDinosaurs are struggling to fend the lethal mechanized fleet\n")
            elif Fleet.Weapon > Herd == True:
                print("\nAnother warrior has fallen in the herd\n")
            else:
                print("\nThe dinosaur herd collapse from exhaustion\n"
                  "\nRobot Fleet were unstoppable with their destructive weapon\n")
