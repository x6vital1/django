from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def user_page(request):
    return render(request, 'user/user_page.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/user/')
        else:
            return HttpResponse('User not found')
    else:
        return render(request, 'user/login.html')


def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name)
        user.save()
        return redirect('/user/login/')
    else:
        return render(request, 'user/registration.html')


def user_logout(request):
    logout(request)
    return redirect('/user/login/')
