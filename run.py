from village import *
from person import *

def main():
        bob = Person("Bob", 22, 'M')
        jane = Person("Jane", 45,'F', False)
        print(bob)
        print(jane)
#     villagers = make_villagers(40)
    


        town = Village("Gulltown", 20)
        town.check_stats()
        town.pop_bin()

#     for i in town.villagers:
#         print(i)



if __name__ == '__main__':
    main()