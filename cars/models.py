from django.db import models
from tires.models import Tires


class Car(models.Model):
    """Cars are the main thing our factory products."""
    name = models.CharField("Car Model", max_length=40)
    year = models.IntegerField("Year", default=2015)
    color = models.CharField("Color", max_length=20, default="White")
    tires = models.ForeignKey(Tires)

    def __str__(self):
        return self.name