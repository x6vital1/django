from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def parcels_page(request):
    return HttpResponse('Parcels page')


def one_parcel_page(request, parcel_id):
    return HttpResponse(f'One parcel page {parcel_id}')
