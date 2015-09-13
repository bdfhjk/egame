from django.db import models

# Create your models here.
class Building(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BuildingState(models.Model):
    building = models.ForeignKey(Building)
    level = models.CharField(max_length=200)

    def __str__(self):
        return str(self.building)
    
