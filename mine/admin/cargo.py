from django.contrib import admin
from mine.models import Cargo


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = [
        'mine', 'tipper',
        'show_max_mass', 'mass', 'sio2', 'fe',
        'has_overload',
        'created'
    ]
    list_filter = ['mine', 'tipper', 'created']

    def has_overload(self, instance):
        return instance.has_overload
    has_overload.boolean = True
    has_overload.short_description = "Перегруз"

    def show_max_mass(self, instance):
        return str(instance.max_mass)
    show_max_mass.short_description = "Макс.груз"

