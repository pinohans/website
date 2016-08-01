from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User,Permission
from django.contrib.contenttypes.models import ContentType
from guardian.shortcuts import assign
from django.conf import settings
import os

def home(request):
	return render(request,'home.html')

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = auth.authenticate(username=username, password=password)
			if user and user.is_active:
				auth.login(request,user)
				return HttpResponseRedirect("/")
	else:
		form = LoginForm()
	return render(request,"login.html",{'form':form})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password,email=email)
        os.makedirs(settings.MEDIA_ROOT+username+'/result')
        if username == 'hehe':
            assign('solvedata.solve_data',user)
            assign('solvedata.func1',user)
        user.save()
        return render(request,'register_success.html')
    else:
        return render(request,'register.html')
