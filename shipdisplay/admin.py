from django.contrib import admin

from .models import SystemDB,PlanetDB,CrewDB
# Register your models here.
admin.site.register(SystemDB)
admin.site.register(PlanetDB)
admin.site.register(CrewDB)
