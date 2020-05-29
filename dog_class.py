
class Dog:

    def __init__(self, name, age, legs, fur_colour):
        self.name = name
        self.age = age
        self.legs = legs
        self.fur_colour = fur_colour

    def sleep(self):
        return 'zzzzzzzzzzz'

    def eat(self, bone):
        return 'nom nom' + bone

    def run(self):
        return 'wooohooooo fun!'

    def rescue_person(self, person):
        brk = ', '
        return "I'll save you, {}".format(person)

    def chase(self, animal):
        return 'GONNA GET CAT! GONNA GET CAT!' + animal


