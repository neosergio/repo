from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, RedirectView
from django.views.generic.edit import FormView
from archive.models import File
from django.utils import timezone

class FileListView(ListView):
    model = File
    context_object_name = "file_list"

class FileDetailView(DetailView):
    model = File

    def get_context_data(self, **kwargs):
        context = super(FileListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class DisplayFileView(TemplateView):
    template_name = "archive/file_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayFileView, self).get_context_data(**kwargs)
        context['file'] = File.objects.get(pk=self.kwargs.get('file_id', None))
        return context

class DisplayRedirectView(RedirectView):

    def get(self, request, *args, **kwargs):
        file_id = self.kwargs.get('file_id', None)
        file = File.objects.get(pk=file_id)
        self.url = '/%s-%s' % (file.id, file.slug)
        return super(DisplayRedirectView, self).get(self, request, *args, **kwargs)

class SuggestionView(FormView):