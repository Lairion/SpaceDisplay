from django.conf.urls import url
from django.contrib import admin
from .views import (base,desktop,crew,description_crew)
urlpatterns = [
    url(r'base$', base, name='base'),
    url(r'desktop$', desktop, name='desktop'),
    url(r'crew/$', description_crew, name='crew'),
    url(r'description_crew/$', description_crew, name='crew'),
]