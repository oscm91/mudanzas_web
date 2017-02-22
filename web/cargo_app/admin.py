from django.contrib import admin
from .models import TxtFile

class CargoAdmin(admin.ModelAdmin):
    pass
admin.site.register(TxtFile, CargoAdmin)