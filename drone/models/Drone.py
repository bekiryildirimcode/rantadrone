from django.db import models
from django.utils.text import slugify
from django_better_admin_arrayfield.models.fields import ArrayField
from drone.models import BrandModel, CategoryModel


class DroneModel(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='media/drone/', blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=False)
    brand = models.ForeignKey(BrandModel,on_delete=models.CASCADE)
    equipment = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    price = models.DecimalField(decimal_places=2, default=0.0, max_digits=8)
    description = models.TextField(blank=True,null=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Drone"
        verbose_name_plural = "Drones"

    def __str__(self):
        return self.name
