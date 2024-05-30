from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def rented_list(request):
    return render(request, 'page/rented.html')
