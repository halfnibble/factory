from django.contrib import admin
from .models import Car, Tires


class CarAdmin(admin.ModelAdmin):
    pass


class TiresAdmin(admin.ModelAdmin):
    pass


admin.site.register(Car, CarAdmin)
admin.site.register(Tires, TiresAdmin)
