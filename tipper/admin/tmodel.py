from django.contrib import admin
from tipper.models import TModel


@admin.register(TModel)
class TModelAdmin(admin.ModelAdmin):
    search_fields = ['title', 'code']
    list_display = ['title', 'code', 'max_mass']
    list_filter = ['max_mass']
