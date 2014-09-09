# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_auto_20140901_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='slug',
            field=models.SlugField(default=datetime.date(2014, 9, 8)),
            preserve_default=False,
        ),
    ]
