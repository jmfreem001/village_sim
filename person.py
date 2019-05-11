from village import *

class Person():
    """Represents a person"""
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
