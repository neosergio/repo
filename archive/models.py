from django.db import models
from os import path

class File(models.Model):
    GROOVY = 'G'
    BUILD_SPECIFICATION = 'B'
    CONFIGURATION = 'C'
    PROPERTY = 'P'
    ARTICLE = 'A'
    FILE_TYPES = (
        (GROOVY, 'Groovy'),
        (BUILD_SPECIFICATION, 'Build Specification'),
        (CONFIGURATION, 'Configuration'),
        (PROPERTY, 'Property'),
        (ARTICLE, 'Article'),
    )
    file_type = models.CharField(max_length=1, choices=FILE_TYPES, default=GROOVY)
    description = models.TextField(help_text="description of the file")
    datafile = models.FileField(upload_to='data', help_text='file to upload')
    datetime = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.description

