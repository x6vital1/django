from django.http import HttpResponse
from django.shortcuts import render
from parcel import models


# Create your views here.
def parcels_page(request):
    parcels = models.Parcel.objects.filter(recipient=request.user)
    return render(request, 'parcels/parcels_page.html', {'parcels': parcels})


def one_parcel_page(request, parcel_id):
    parcel = models.Parcel.objects.get(pk=parcel_id)
    return render(request, 'parcels/one_parcel_page.html', {'parcel': parcel})
