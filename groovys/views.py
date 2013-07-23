from groovys.models import File
from groovys.forms import FileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from datetime import datetime

login_url_redirection = '/login'

def index(request):
	files = File.objects.all()
	return render_to_response(
		'index.html', 
		{'files': files}, 
		context_instance=RequestContext(request))

@login_required(login_url = login_url_redirection)
def new(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			groovy_tmp = form.save(commit=False)
			groovy_tmp.register = request.user
			groovy_tmp.datetime = datetime.now()
			groovy_tmp.save()
			redirection = '/'
			return HttpResponseRedirect(redirection)
	else:
		form = FileForm()
	return render_to_response(
		'new_groovy.html', 
		{'form':form}, 
		context_instance=RequestContext(request))

def login_view(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			login_user = request.POST['username']
			login_pass = request.POST['password']
			login_access = authenticate(username=login_user, password=login_pass)
			if login_access is not None:
				if login_access.is_active:
					login(request, login_access)
					return HttpResponseRedirect('/')
	else:
		form = AuthenticationForm()
	return render_to_response(
		'login.html',
		{'form': form},
		context_instance = RequestContext(request))

@login_required(login_url = login_url_redirection)
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')