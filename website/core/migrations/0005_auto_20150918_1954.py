# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150918_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='production',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='resource',
            field=models.ForeignKey(blank=True, to='core.Resource', null=True),
        ),
    ]
