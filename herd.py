from dinosaurs import Dinosaurs

dinosaurs = Dinosaurs()

class Herd:
    def __int__(self):
        self.dinosaurs = {}

    def create_herd(self):
        first_dinosaur = 'Sharptooth'
        second_dinosaur = 'Steelhorn'
        third_dinosaur = 'Longneck'

        self.dinosaurs.append(first_dinosaur)
        self.dinosaurs.append(second_dinosaur)
        self.dinosaurs.append(third_dinosaur)
