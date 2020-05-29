
class Cat:

    def __init__(self, name, age, legs, fur):
        self.name = name
        self.age = age
        self.legs = legs
        self.fur = fur

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