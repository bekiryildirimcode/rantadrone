from django.urls import path
from . import views

app_name = "drone"

urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('rent/<slug:slug>', views.RentDroneView.as_view(), name='rent'),
        path('drons/', views.DroneListView.as_view(), name='drone-list'),
]