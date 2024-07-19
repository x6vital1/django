from django.http import HttpResponse
from django.shortcuts import render
from post_machine import models


# Create your views here.
def locker_view(request, machine_id):
    one_post_machine = models.PostMachine.objects.get(pk=machine_id)
    post_machine_locker = models.Locker.objects.filter(post_machine=one_post_machine)
    one_locker = models.Locker.objects.get(pk=5)
    return HttpResponse(f'Адрес: {one_post_machine.address}. Всего ящиков: {post_machine_locker.count()}.')
