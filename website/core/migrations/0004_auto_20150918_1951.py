# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_building_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingResourceLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('production', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JobState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='production',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='buildingstate',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobstate',
            name='building',
            field=models.ForeignKey(to='core.Building'),
        ),
        migrations.AddField(
            model_name='jobstate',
            name='citizen',
            field=models.ForeignKey(to='core.Citizen', unique=True),
        ),
        migrations.AddField(
            model_name='citizen',
            name='education',
            field=models.ForeignKey(to='core.Education'),
        ),
        migrations.AddField(
            model_name='citizen',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AddField(
            model_name='buildingresourcelevel',
            name='building',
            field=models.ForeignKey(to='core.Building'),
        ),
        migrations.AddField(
            model_name='building',
            name='resource',
            field=models.ForeignKey(to='core.Resource', null=True),
        ),
    ]
