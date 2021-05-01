from robots import Robots

robots = Robots()

class Fleet:
    def __int__(self):
        self.robots = {}

    def create_fleet(self):
        first_robot_soldier = 'Bubble Bee'
        second_robot_soldier = 'Ironhide'
        third_robot_soldier = 'Optimus Prime'

        self.robots.append(first_robot_soldier)
        self.robots.append(second_robot_soldier)
        self.robots.append(third_robot_soldier)
