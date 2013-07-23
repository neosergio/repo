from django.contrib.auth.models import User
from django.db import models
from os import path

class File(models.Model):
	description = models.TextField(
		help_text = 'explicit description of the file')
	register = models.ForeignKey(User)
	groovy_file = models.FileField(
		upload_to = 'groovys',
		help_text = 'file with groovy script')
	datetime = models.DateTimeField()

	def file_link(self):
		if self.groovy_file:
			print self.groovy_file.url
			return "<a class='btn btn-primary' href='%s'>download</a>" % (self.groovy_file.url,)
		else:
			return "No attachment"

	file_link.allow_tags = False

