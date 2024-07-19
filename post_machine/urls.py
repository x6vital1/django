from django.urls import path

import post_machine.views

urlpatterns = [
    path('', post_machine.views.post_machines_view),
    path('<post_id>', post_machine.views.one_post_machine_view),
]