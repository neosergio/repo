# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='datetime',
            field=models.DateTimeField(auto_now=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=models.CharField(default=b'G', max_length=1, choices=[(b'G', b'Groovy'), (b'B', b'Build Specification'), (b'C', b'Configuration'), (b'P', b'Property'), (b'A', b'Article')]),
        ),
    ]
