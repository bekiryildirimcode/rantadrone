from django.db import models
from django.utils.text import slugify


class BrandModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


    def __str__(self):
        return self.title