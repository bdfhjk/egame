from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Building(models.Model):
    number = models.IntegerField() #Proper displaying
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    resource = models.ForeginKey(Resource, null=True)
    production = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class BuildingState(models.Model):
    user = models.ForeginKey(User, unique=True)
    building = models.ForeignKey(Building)
    level = models.CharField(max_length=200)

    def __str__(self):
        return str(self.building)

class BuildingResourceLevel(models.Model):  #How much what resource on each level
    building = models.ForeginKey(Building)
    level = models.IntegerField()
    production = models.IntegerField(null=True)

    def __str__(self):
        return str(self.building) + " - " + str(self.level)

class Education(models.Model):
    number = models.IntegerField() #Proper displaying
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class JobState(models.Model):
    citizen = models.ForeginKey(Citizen, unique=True)
    building = models.ForeginKey(Building)

    def __str__(self):
        return str(self.citizen) + " - " + str(self.building)

class Citizen(models.Model):
    user = models.ForeginKey(User, unique=True)
    education = models.ForeginKey(Education)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    
    
