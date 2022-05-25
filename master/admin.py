from django.contrib import admin

from master.models import Master, MasterPost, ServiceCategory, MasterService


class MasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'phone_number', 'email', 'user', 'is_activated')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'location', 'phone_number', 'email', 'user', 'is_activated')
    list_editable = ('is_activated',)
    list_filter = ('time_create', 'is_activated')
    prepopulated_fields = {"slug": ("name",)}

class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug', 'description')
    list_filter = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description', 'custom_category', 'serviceCategory', 'master')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug', 'custom_category', 'serviceCategory', 'master')
    list_filter = ('name', 'slug', 'custom_category', 'serviceCategory', 'master')
    prepopulated_fields = {"slug": ("name",)}




admin.site.register(Master, MasterAdmin)
admin.site.register(MasterPost)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(MasterService, ServiceAdmin)