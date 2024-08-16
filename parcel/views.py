import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from parcel import models
from django.views import View


# Create your views here.
def parcels_page(request):
    parcels = models.Parcel.objects.filter(recipient=request.user)
    return render(request, 'parcels/parcels_page.html', {'parcels': parcels})


def one_parcel_page(request, parcel_id):
    parcel = models.Parcel.objects.get(pk=parcel_id)
    return render(request, 'parcels/one_parcel_page.html', {'parcel': parcel})


class GetParcel(View):
    def post(self, request, parcel_id):
        parcel = models.Parcel.objects.get(pk=parcel_id)
        parcel.status = True
        parcel.open_datetime = datetime.datetime.now()
        if parcel.open_datetime is None:
            parcel.open_datetime = datetime.datetime.now()
        parcel.save()
        parcel.locker.status = True
        parcel.locker.save()
        return redirect('/user/')
