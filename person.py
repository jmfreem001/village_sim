from village import *

class Person():
    """Represents a person"""
    def __init__(self, name, age, gender, village, alive=True):
        self.name = name
        self.age = age
        self.gender = gender
        self.alive = alive
        self.village = village
    
    def __str__(self):
        if self.alive:
            return '{self.name} of {self.village.name}({self.gender}) is {self.age}.'.format(self=self)
        else:
            return '{self.name} of {self.village.name}({self.gender}) died at age {self.age}.'.format(self=self)
    def kill(self):
        """simulates death of a Person"""
        # set as not alive
        self.alive = False
        self.village.population -= 1
        print("{self.name} of {self.village.name} has died").format(self=self)
        # remove from villagers
        self.village.villagers.remove(self)
        # Add person to graveyard
        self.village.graveyard.append(self)

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

def rand_person(village):
    """Randomly generates a simulation of a person"""
    gen = rand_gen()
    age = randint(0, 55)
    name = rand_name(gen)
    vil = village
    return Person(name, age, gen, vil)
