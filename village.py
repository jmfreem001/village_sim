from random import randint

from person import *


class Village():
    """represents a village"""

    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.villagers = make_villagers(population)
        self.morale = 50
        self.resources = 50
        self.aggressiveness = 50

    def check_stats(self):
        """Checks the attributes of selected village"""
        print(self.name)
        print("Morale: " + str(self.morale))
        print("Population: " + str(self.population))
        print("Resources: " + str(self.resources))
        print("Aggressiveness: " + str(self.aggressiveness))
    
    def pop_bin(self):
        """counts each gender and each age group"""
        male = 0
        female = 0
        children = 0
        adults = 0 
        elders = 0
        for i in self.villagers:
            if i.gender == 'M':
                male += 1
            else:
                female += 1
            if i.age < 13:
                children += 1
            elif i.age < 41:
                adults += 1
            else:
                elders += 1
        print("Gender: There are {male} males and {female} females in the village.").format(male=male, female=female)
        print("Age Groups: There are {children} children and {adults} adults and {elders} elders in the village.").format(children=children, adults=adults, elders=elders)



def make_villagers(n):
    """Creates n number of people objects that are residents of the village."""
    villagers = []
    for i in range(0, n):
        x = rand_person()
        villagers.append(x)
    return villagers




