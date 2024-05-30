from django.contrib import admin
from .models import RentedModel
from django.utils.html import format_html

@admin.register(RentedModel)
class RentedAdmin(admin.ModelAdmin):
    model = RentedModel
    fields = ['drone','user','start_date','start_time','end_date','end_time']
    list_display = ('drone', 'user', "start_date", "start_time", 'end_date', 'end_time')
    search_fields = ('drone__name','user__name')
    list_filter = ('drone__name','user__name')