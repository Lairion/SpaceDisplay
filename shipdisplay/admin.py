from django.contrib import admin

from .models import SystemDB,PlanetDB,CrewDB,PeopleDB
# Register your models here.
admin.site.register(SystemDB)
admin.site.register(PlanetDB)
admin.site.register(PeopleDB)
admin.site.register(CrewDB)
