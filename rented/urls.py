from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.rented_list, name='rented_list'), # Only template render
    path('api/',include('rented.api.urls')) # Update and deletion of drones rented by the user
]