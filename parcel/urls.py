from django.urls import path

import parcel.views
urlpatterns = [
    path('', parcel.views.parcels_page, name='parcels_page'),
    path('get_parcel/<int:parcel_id>/', parcel.views.GetParcel.as_view(), name='get_parcel'),
    path('<parcel_id>/', parcel.views.one_parcel_page, name='one_parcel_page'),


]
