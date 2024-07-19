from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def post_machines_view(request):
    return HttpResponse('Post machines page')


def one_post_machine_view(request, post_id):
    return HttpResponse(f'One post machine {post_id}')
