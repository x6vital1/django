from django.urls import path

import parcel.views

urlpatterns = [
    path('', parcel.views.parcels_page),
    path('<parcel_id>', parcel.views.one_parcel_page)

]
