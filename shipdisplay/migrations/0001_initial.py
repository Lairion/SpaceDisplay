# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrewDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('Capitan', 'Capitan'), ('Mechanik', 'Mechanik'), ('Pilot', 'Pilot'), ('Passenger', 'Passenger'), ('Medic', 'Medic'), ('Soldier', 'Soldier')], max_length=20)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeopleDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Alive', 'Alive'), ('Dead', 'Dead')], max_length=20)),
                ('conviction', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=20)),
                ('conviction_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('profession', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='people/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='PlanetDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planet_name', models.CharField(max_length=100)),
                ('size_planet', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=20)),
                ('color_planet', models.CharField(max_length=20)),
                ('population', models.IntegerField(max_length=100)),
                ('planet_position', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='SystemDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_system', models.CharField(max_length=100)),
                ('how_many_planets', models.IntegerField(max_length=3)),
                ('color_star', models.CharField(max_length=100)),
                ('pos_x', models.IntegerField(max_length=10)),
                ('pos_y', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='planetdb',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipdisplay.SystemDB'),
        ),
        migrations.AddField(
            model_name='crewdb',
            name='people_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipdisplay.PeopleDB'),
        ),
    ]
