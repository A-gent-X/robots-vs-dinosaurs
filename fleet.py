from robots import Robots

class Fleet:
    def __int__(self):
        self.robots = {}

    def create_fleet(self):
        first_robot_soldier = ({1: 'Bubble Bee'})
        second_robot_soldier = ({2: 'Ironhide'})
        third_robot_soldier = ({3: 'Optimus Prime'})

        self.robots.append(first_robot_soldier)
        self.robots.append(second_robot_soldier)
        self.robots.append(third_robot_soldier)



