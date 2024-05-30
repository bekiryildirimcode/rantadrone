from django.db import models

from accounts.models import CustomUser
from drone.models import DroneModel


class RentedModel(models.Model):
    id = models.AutoField(primary_key=True)
    drone = models.ForeignKey(DroneModel, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = "Rented"
        verbose_name_plural = "Rented"

    def __str__(self):
        return self.drone.name
