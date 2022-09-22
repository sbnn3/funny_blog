from django.contrib import admin
from .models import Guitars


@admin.register(Guitars)
class GuitarsAdmin(admin.ModelAdmin):
    """
    Guitars Model to Admin Panel
    """
    prepopulated_fields = {'slug': ('guitar_model',)}
    list_display = ('artist', 'guitar_model', 'status', 'price', 'created_on')
    list_filter = ('artist', 'created_on')
    search_fields = ['guitar_model', 'artist']
    actions = ['publish_guitar']

    def publish_guitar(self, request, queryset):
        queryset.update(status=1)