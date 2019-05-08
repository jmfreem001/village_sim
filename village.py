class Person():

    def __init__(self, name, age, gender, alive=True):
        self.name = name
        self.age = age
        self.gender = gender
        self.alive = alive
    
    def __str__(self):
        if self.alive:
            return '{self.name}({self.gender}) is {self.age}.'.format(self=self)
        else:
            return '{self.name}({self.gender}) died at age {self.age}.'.format(self=self)


class Village():
    """represents a village"""

    def __init__(self, name, population):
        self.name = name
        self.population = population
        # self.villagers = make_villagers(population)
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
        print("\n")


def make_villagers(n):
    """Creates n number of people objects that are residents of the village."""
    villagers = []
    # TODO Randomize the generation of villagers
    # ran_gender()
    # ran_name if gender male use mail list to generate else female name list
    # ran age

town = Village("Gulltown", 20)
town.check_stats()
bob = Person("Bob", 22, 'M')
jane = Person("Jane", 45,'F', False)

print(bob)
print(jane)