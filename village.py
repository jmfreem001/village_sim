from random import randint

from person import *


class Village():
    """represents a village"""

    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.villagers = make_villagers(self, population)
        self.food = population * 2
        self.shelter = population
        self.morale = 50
        self.wealth = 250
        self.might = 5
        self.defense = 0
        self.graveyard = []

    def check_stats(self):
        """Checks the attributes of selected village"""
        print(self.name)
        print("Population: " + str(self.population))
        print("Wealth: " + str(self.wealth))
        print("Morale: " + str(self.morale))
        print("Food:"+ str(self.food))
        print("Shelter:"+ str(self.shelter))
        print("Might: " + str(self.might))
        print("Defense: "+ str(self.defense))

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



def make_villagers(self, n):
    """Creates n number of people objects that are residents of the village."""
    villagers = []
    for i in range(0, n):
        # need to assign village to person for grave yard and naming purposes. 
        x = rand_person(self)
        villagers.append(x)
    return villagers




