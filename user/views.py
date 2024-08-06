from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from parcel import models
from user.forms import LoginForm, RegisterForm
from django.views import View


# Create your views here.

def user_page(request):
    if request.user.is_authenticated:
        parcels = models.Parcel.objects.filter(recipient=request.user)
        return render(request, 'user/user_page.html', {'parcels': parcels})
    else:
        return redirect('/user/login/')


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html', context={'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/user/')
        return render(request, 'user/login.html', context={'form': form, 'error': 'Invalid username or password'})


class UserRegistration(View):
    def get(self, request):
        return render(request, 'user/registration.html', context={'form': RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'])
            user.save()
            return redirect('/user/login/')
        return render(request, 'user/registration.html', context={'form': RegisterForm(), 'error': form.errors})




class UserLogout(View):
    def post(self, request):
        logout(request)
        return redirect('/user/login/')
