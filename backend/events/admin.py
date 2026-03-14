from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "start_datetime", "is_featured")
    search_fields = ("title", "short_description")
    prepopulated_fields = {"slug": ("title",)}