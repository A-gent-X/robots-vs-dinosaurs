from dinosaurs import Dinosaur

class Herd:
    def __int__(self):
        self.dinosaurs = {}

    def create_herd(self):
        first_dinosaur = ({1:'Sharptooth'})
        second_dinosaur = ({2: 'Steelhorn'})
        third_dinosaur = ({3: 'Longneck'})

        self.dinosaurs.append(first_dinosaur)
        self.dinosaurs.append(second_dinosaur)
        self.dinosaurs.append(third_dinosaur)
