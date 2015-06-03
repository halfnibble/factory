from django.db import models

class Tires(models.Model):
    """Tires typically go on cars."""
    name = models.CharField("Brand Name", max_length=40)
    size = models.FloatField("Tire R", default=17.0)


class Car(models.Model):
    """Cars are the main thing our factory products."""
    name = models.CharField("Car Model", max_length=40)
    year = models.IntegerField("Year", max_length=4, default=2015)
    color = models.CharField("Color", max_length=20, default="White")
    tires = models.ForeignKey(Tires)