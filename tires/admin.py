from django.contrib import admin
from .models import Tires


class TiresAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tires, TiresAdmin)
