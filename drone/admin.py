from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from .models import CategoryModel, BrandModel, DroneModel
from django.utils.html import format_html

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    model = CategoryModel
    fields = ['title']
    search_fields = ('title',)
    list_filter = ('title',)



@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    model = BrandModel
    fields = ['title']
    search_fields = ('title',)
    list_filter = ('title',)



@admin.register(DroneModel)
class DroneAdmin(admin.ModelAdmin, DynamicArrayMixin):
    model = DroneModel
    fields = ['image', 'name', 'category', 'brand','price', 'description', 'equipment', 'status']
    list_display = ('display_image', 'name',"category", "brand",'price','status')
    list_filter = ('name', 'category','brand','price')
    search_fields = ('name', 'category__title','brand__title')

    def display_image(self, obj):
        return format_html('<img src="{}" width="30" height="30" />'.format(obj.image.url))
