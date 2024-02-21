from django.contrib import admin
from .models import Car
from django.utils.html import format_html


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(object.car_photo.url))
    thumbnail.short_description = 'Car Image'

    list_display = ['id', 'car_title', 'thumbnail', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured']
    list_filter = ['city', 'model', 'body_style', 'fuel_type', 'year']
    list_display_links = ['id', 'car_title', 'thumbnail']
    search_fields = ['id', 'car_title', 'city', 'model', 'body_style', 'fuel_type', 'color']
    list_editable = ['is_featured']


