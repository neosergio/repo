# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_type', models.CharField(default=(b'G',), max_length=1, choices=[((b'G',), b'Groovy'), (b'B', b'Build Specification'), (b'C', b'Configuration'), (b'P', b'Property'), (b'A', b'Article')])),
                ('description', models.TextField(help_text=b'description of the file')),
                ('datafile', models.FileField(help_text=b'file to upload', upload_to=b'data')),
                ('datetime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
