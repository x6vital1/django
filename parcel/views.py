from django.http import HttpResponse
from django.shortcuts import render
from parcel import models


# Create your views here.
def parcels_page(request):
    return HttpResponse('Parcels page')


def one_parcel_page(request, parcel_id):
    parcel = models.Parcel.objects.get(pk=parcel_id)
    return HttpResponse(f'Parcel: {parcel}')
