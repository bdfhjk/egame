# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='desc',
            field=models.CharField(max_length=200, default='empty'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buildingstate',
            name='level',
            field=models.CharField(max_length=200),
        ),
    ]
