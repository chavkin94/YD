from django.contrib import admin

from master.models import Master


class MasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'phone_number', 'email', 'user', 'is_activated')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'location', 'phone_number', 'email', 'user', 'is_activated')
    list_editable = ('is_activated',)
    list_filter = ('time_create', 'is_activated')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Master, MasterAdmin)