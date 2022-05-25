from django.contrib import admin

from main.models import *

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Location, LocationAdmin)
admin.site.register(LocationDistrict)
admin.site.register(LocationRegions)
admin.site.register(LocationСity)
