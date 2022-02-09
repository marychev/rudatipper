from django.contrib import admin
from mine.models import Mine


@admin.register(Mine)
class MineAdmin(admin.ModelAdmin):
    pass
