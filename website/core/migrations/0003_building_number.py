# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150912_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
