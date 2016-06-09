from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SystemDB(models.Model):
    name_system = models.CharField(max_length=100)
    how_many_planets = models.IntegerField(max_length=3)
    color_star = models.CharField(max_length=100)
    pos_x = models.IntegerField(max_length=10)
    pos_y = models.IntegerField(max_length=10)

class PlanetDB(models.Model):
    SIZE_PLANET = (("S","Small"),("M","Medium"),("L","Large"))
    system = models.ForeignKey(SystemDB)
    planet_name = models.CharField(max_length=100)
    size_planet = models.CharField(max_length=20, choices=SIZE_PLANET)
    color_planet = models.CharField(max_length=20)
    population = models.IntegerField(max_length=100)
    planet_position = models.IntegerField(max_length=3)

class PeopleDB(models.Model):
    STATUS = (("Alive","Alive"),("Dead","Dead"))
    CONVICTION = (("True","True"),("False","False"))
    #planet = models.ForeignKey(PlanetDB)
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=100)
    species = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS)
    conviction = models.CharField(max_length=20, choices=CONVICTION)
    conviction_description = models.TextField(max_length=1000,null=True,blank=True)
    profession = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="people/%Y/%m/%d")
    def __str__(self):
        return self.name;
        
    
class CrewDB(models.Model):
    JOB_NAME=(("Capitan","Capitan"),("Mechanik","Mechanik"),("Pilot","Pilot"),("Passenger","Passenger"),("Medic","Medic"),("Soldier","Soldier"))
    people_id = models.ForeignKey(PeopleDB)
    position = models.CharField(max_length=20, choices=JOB_NAME)
    location = models.CharField(max_length=20,null=True, blank=True)
    
    
    
    


		

