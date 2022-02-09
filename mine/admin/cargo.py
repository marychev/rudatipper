from django.contrib import admin
from mine.models import Cargo


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass
