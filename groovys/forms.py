from groovys.models import File
from django.forms import ModelForm

class FileForm(ModelForm):
	class Meta:
		model = File
		exclude = ('register', 'datetime')