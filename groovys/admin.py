from django.contrib import admin
from groovys.models import File

class FileAdmin(admin.ModelAdmin):
	list_display = ('description', 'register', 'file_link', 'datetime')

admin.site.register(File, FileAdmin)