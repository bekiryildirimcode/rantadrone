# views.py
from django.views.generic import ListView
from drone.models import DroneModel
from drone.forms import DroneFilterForm
from rented.models import RentedModel
from django.db.models import Q


class DroneListView(ListView):
    model = DroneModel
    template_name = 'page/list.html'
    context_object_name = 'drones'
    paginate_by = 10

    def get_queryset(self):
        queryset = DroneModel.objects.none()
        form = DroneFilterForm(self.request.GET)
        if form.is_valid():
            queryset = DroneModel.objects.all()
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            brand = form.cleaned_data.get('brand')

            if start_date and end_date and brand:

                # This query returns the ids of drones rented within a specific date range.
                excluded_ids = RentedModel.objects.filter(
                    Q(start_date__gte=start_date), Q(end_date__lte=end_date)
                ).values_list('drone', flat=True)
                # Returns records that are excluded from this query
                queryset = queryset.exclude(id__in=excluded_ids).filter(brand=brand)

            if start_date and end_date:
                excluded_ids = RentedModel.objects.filter(
                    Q(start_date__gte=start_date), Q(end_date__lte=end_date)
                ).values_list('drone', flat=True)
                queryset = queryset.exclude(id__in=excluded_ids)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DroneFilterForm(self.request.GET)
        return context
