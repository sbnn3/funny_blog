from django.contrib import admin
from .models import Guitars


@admin.register(Guitars)
class GuitarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('guitar_model',)}
    list_display = ('artist', 'guitar_model', 'price', 'created_on')
    list_filter = ('artist', 'created_on')
    search_fields = ['guitar_model', 'artist']


