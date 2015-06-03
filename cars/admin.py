from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Car, CarAdmin)

