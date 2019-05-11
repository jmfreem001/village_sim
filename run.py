from village import *
from person import *


def main():
	# Create user village.       
	my_town = Village("Gulltown", 2)
	# Print initial stats
	stats(my_town)
	peeps = my_town.villagers
	x = randint(0,len(peeps)-1)
	person = peeps[x]
	person.kill()
	# Print post death stats
	stats(my_town)

def stats(town):
	# Print initial stats
	town.check_stats()
    # SHow gender and age group breakdown. 
	town.pop_bin()
	for i in town.villagers:
		print(i)


if __name__ == '__main__':
    main()

