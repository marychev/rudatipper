from django.contrib import admin
from tipper.models import Tipper


@admin.register(Tipper)
class TipperAdmin(admin.ModelAdmin):
    search_fields = ['number', 'tmodel__title']
    list_display = ['id', 'number', 'tmodel']
    list_display_links = ['id', 'number']
    list_filter = ['tmodel']
