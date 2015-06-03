from django.db import models


class Tires(models.Model):
    """Tires typically go on cars."""
    name = models.CharField("Brand Name", max_length=40)
    size = models.FloatField("Tire R", default=17.0)

    def __str__(self):
        return u"{0}-R{1}".format(self.name, self.size)

    class Meta:
        verbose_name_plural = "Tires"

