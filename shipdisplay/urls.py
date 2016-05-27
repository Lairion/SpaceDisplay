from django.conf.urls import url
from django.contrib import admin
from .views import (base,desktop)
urlpatterns = [
    url(r'base$', base, name='base'),
    url(r'desktop$', desktop, name='desktop'),
]