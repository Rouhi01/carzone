from django.contrib import admin
from .models import Team
from django.utils.html import format_html

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))
    thumbnail.short_description = 'Photo'

    list_display = ['id', 'thumbnail', 'first_name', 'designation', 'created_at', 'updated_at']
    list_display_links = ['id', 'first_name', 'thumbnail']
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['designation']



