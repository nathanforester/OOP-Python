# import classes, initialise objs and run methods here
# Separation of concerns

from dog_class import *
from cat_class import *

rex_instance = Dog(name='ben')
print(rex_instance)
print(type(rex_instance))

mitten_instance = Cat()
print(mitten_instance)
print(type(mitten_instance))

print(rex_instance.sleep())
print(rex_instance.chase('MEOW!'))
print(rex_instance.eat('gnaw bone'))
print(rex_instance.run())
print(rex_instance.rescue_person('Nathan'))

print(mitten_instance.run())
print(mitten_instance.chase('dog', 'woof'))
print(mitten_instance.ignore())
print(mitten_instance.fight('dog'))
print(mitten_instance.purr())

print(rex_instance.get_dog_age())

print(rex_instance.get_dog_age())

rex_instance.dog_birthday_incrementer()

print(rex_instance.get_dog_age())

rex_instance.dog_birthday_incrementer()

print(rex_instance.get_dog_age())