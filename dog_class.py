from animal_class import *

class Dog:

    def __init__(self, name='', age=0, legs='', fur_colour=''):
        self.__name = name
        self.__dog_age = age
        self.__human_age = 0
        self.legs = ''
        self.fur_colour = ''

    def get_dog_age(self):
        return self.__dog_age

    def __increase_dog__and_human_years(self):
        self.__human_age += 1
        self.__dog_age += 7

    def dog_birthday_incrementer(self):
        print(f'happy birthday! You are a GOOD BOY! GOOD BOY {self.__name}!')
        self.__increase_dog__and_human_years()
        return f'dog years at {self.__dog_age} and human years {self.__human_age}'

    def sleep(self):
        return 'zzzzzzzzzzz'

    def eat(self, bone):
        return 'nom nom' + bone

    def run(self):
        return 'wooohooooo fun!'

    def rescue_person(self, person):
        return "I'll save you, {}".format(person)

    def chase(self, animal):
        return f'GONNA GET {animal}! GONNA GET {animal}!'

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name
        return True


