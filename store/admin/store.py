from django.contrib import admin
from store.models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass
