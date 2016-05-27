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


		

