from django.contrib import admin
from tipper.models import TModel


@admin.register(TModel)
class TModelAdmin(admin.ModelAdmin):
    pass
