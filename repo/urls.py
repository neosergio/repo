from django.conf.urls import patterns, include, url
from django.contrib import admin
from archive.views import FileListView, FileDetailView
from django.views.generic import TemplateView, DetailView
from django.views.generic import ListView
from archive.views import DisplayFileView, DisplayRedirectView, SuggestionView
from archive.models import File

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'repo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<file_id>\d+)/$', DisplayRedirectView.as_view()),
    url(r'^(?P<file_id>\d+)-(?P<slug>[-\w]+)/$', DisplayFileView.as_view(), name="files_view"),
    url(r'^sugerencia/$', SuggestionView.as_view()),
    url(r'^$', ListView.as_view(
        model = File,
        paginate_by = 2,
        queryset = File.objects.all(),
        context_object_name = "files",
        template_name='archive/index.html'),
    ),

)
