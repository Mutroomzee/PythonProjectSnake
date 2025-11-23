import random

name = [
    'Vasya',
    'Kolya',
    'Igor',
    'SuperYurii',
    'Goga'
]
pogon = [
    'Durnoi',
    'Dikiy',
    'Tupoi',
    'Chetkiy',
    'Urod'
]
def create_name(name , pogon):
    return random.choice(name) + '' + random.choice(pogon)

print(create_name(name, pogon))