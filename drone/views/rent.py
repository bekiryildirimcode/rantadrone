from django.http import JsonResponse
from django.views.generic import DetailView

from drone.forms import RentDroneForm
from drone.models import DroneModel
from django.contrib.auth.mixins import LoginRequiredMixin

from rented.models import RentedModel

class RentDroneView(LoginRequiredMixin,DetailView):

    login_url = '/accounts/login/'
    http_method_names = ['get', 'post']
    model = DroneModel
    template_name = 'page/rent_drone.html'
    context_object_name = 'drone'
    slug_field = 'slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RentDroneForm()
        return context

    def post(self, request,slug):
        self.object = self.get_object()
        form = RentDroneForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            start_time = form.cleaned_data.get('start_time')
            end_date = form.cleaned_data.get('end_date')
            end_time = form.cleaned_data.get('end_time')
            rented = RentedModel.objects.create(drone=DroneModel.objects.get(slug=slug),start_date=start_date, start_time=start_time,
                                                     end_date=end_date, end_time=end_time, user=request.user)
            rented.save()
            return JsonResponse({"message": "Rezervasyon oluşturuldu"})
        else:
            error_message = dict(
                [(key, [error for error in value]) for key, value in form.errors.items()])
            return JsonResponse({"message": error_message } , status=400)

        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)



