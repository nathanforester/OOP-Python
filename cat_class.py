from animal_class import *


class Cat:

    def __init__(self, name='mitten', owner='Nathan'):
        super().__init__()
        self.name = name
        self.owner = owner


    def run(self):
        return 'wooohooooo fun!'

    def chase(self, animal, noise):
        return 'GONNA GET ' + animal + ' ' + 'GONNA GET ' + noise + '!'

    def ignore(self):
        return "I'm not here, silly human"

    def purr(self):
        return 'prrrrrrrprrrrrrrprrrrrrpprrrrrr'

    def fight(self, animal):
        return 'this is my territory {}'.format(animal)