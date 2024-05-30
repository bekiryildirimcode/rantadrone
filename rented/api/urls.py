from django.urls import path
from . import views

urlpatterns = [

    path('rented/', views.RentedList.as_view(), name='rented_data'),
    path('rented/<int:pk>/', views.RentedAction.as_view(), name='rented_action'),

]