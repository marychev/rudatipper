from django.contrib import admin
from store.models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['title', 'polygon', 'max_mass', 'mass', 'sio2', 'fe']
    readonly_fields = ['parse_polygon']
