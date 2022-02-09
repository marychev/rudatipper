from django.contrib import admin
from store.models import History


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass
