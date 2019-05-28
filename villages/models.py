from django.db import models

class Village(models.Model):
    """represents a village"""

    name = models.CharField(max_length=50)
    population = models.IntegerField()
    food = models.IntegerField()
    shelter = models.IntegerField()
    morale = models.IntegerField()
    wealth = models.IntegerField()
    might = models.IntegerField()
    defense = models.IntegerField()

    def __str__(self):
        """Return a string representing a village"""
        return self.name



class Villager(models.Model):
    """Represents a villager"""
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=8)
    alive = models.BooleanField()
    village = models.ForeignKey(Village, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of a villager"""
        if self.alive:
            return '{self.name} of {self.village.name}({self.gender}) is {self.age}.'.format(self=self)
        else:
            return '{self.name} of {self.village.name}({self.gender}) died at age {self.age}.'.format(self=self)
