
class Animal:

    def __init__(self, species, limbs):
        self.species = species
        self.limbs = limbs

    def sleep(self):
        return 'zzzzzzzzzzz'

    def eat(self, food):
        return 'nom nom' + food

    def run(self):
        return 'wooohooooo fun!'


