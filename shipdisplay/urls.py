from django.conf.urls import url
from django.contrib import admin
from .views import (base,desktop,description_crew)
urlpatterns = [
    url(r'base$', base, name='base'),
    url(r'desktop$', desktop, name='desktop'),
    url(r'description_crew/$', description_crew, name='description_crew'),
]