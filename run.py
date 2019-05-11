from village import *
from person import *


def main():
	# Create user village.       
	my_town = Village("Gulltown", 2)
	# Print initial stats
	stats(my_town)

	neighbors = make_village(3)
	for i in neighbors:
		stats(i)
	
	# rand_kill(my_town)
	# print("")
	# # Print post death stats
	# stats(my_town)


def stats(town):
	# Print initial stats
	town.check_stats()
    # SHow gender and age group breakdown. 
	# town.pop_bin()
	# for i in town.villagers:
	# 	print(i)

def rand_kill(town):
	villagers = town.villagers
	x = randint(0,len(villagers)-1)
	person = villagers[x]
	person.kill()

if __name__ == '__main__':
    main()

