from django.contrib import admin
from tipper.models import Tipper


@admin.register(Tipper)
class TipperAdmin(admin.ModelAdmin):
    pass
