from random import randint


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
    def kill(self):
        """simulates death of a Person"""
        self.alive = False
        

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

def rand_gen():
    """Randomly assigns a gender"""
    x = randint(1, 100)
    if x < 51:
        return 'M'
    else:
        return 'F'

def rand_name(gen):
    """Generates a random name from a list of names based on gender."""
    if gen == 'M':
        file = 'mnames.txt'
    else:
        file = 'fnames.txt'
    # Return a random name from a names file. 
    return rand_list_item(file)

    
def rand_list_item(file):
    """Converts a file to a list and returns a random item from the list"""
    with open(file) as infile:
        lines = infile.readlines()
        x = randint(0,len(lines)-1)
        item = lines[x]
        return item

def rand_person():
    """Randomly generates a simulation of a person"""
    gen = rand_gen()
    age = randint(0, 55)
    name = rand_name(gen)
    return Person(name, age, gen)



town = Village("Gulltown", 20)
town.check_stats()
town.pop_bin()

for i in town.villagers:
    print(i)

# bob = Person("Bob", 22, 'M')
# jane = Person("Jane", 45,'F', False)

# print(bob)
# print(jane)
# villagers = make_villagers(40)
