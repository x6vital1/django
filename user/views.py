from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from parcel import models
from user.forms import LoginForm, RegisterForm


# Create your views here.

def user_page(request):
    if request.user.is_authenticated:
        parcels = models.Parcel.objects.filter(recipient=request.user)
        return render(request, 'user/user_page.html', {'parcels': parcels})
    else:
        return redirect('/user/login/')


def user_login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/user/')
            context['error'] = 'Invalid username or password'
    context['form'] = LoginForm()
    return render(request, 'user/login.html', context=context)


def user_registration(request):
    if request.method == 'POST':
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
    else:
        return render(request, 'user/registration.html', context={'form': RegisterForm()})


def user_logout(request):
    logout(request)
    return redirect('/user/login/')
