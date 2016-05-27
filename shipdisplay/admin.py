from django.contrib import admin

from .models import SystemDB,PlanetDB
# Register your models here.
admin.site.register(SystemDB)
admin.site.register(PlanetDB)
