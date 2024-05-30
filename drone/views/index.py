from django.core.paginator import Paginator
from django.shortcuts import render

from django.shortcuts import render
from django.views import View

from drone.models import DroneModel, BrandModel


class IndexView(View):
    http_method_names = ['get']

    def get(self, request):
        brands = BrandModel.objects.all()
        return render(request, 'page/home.html', {'brands': brands})

