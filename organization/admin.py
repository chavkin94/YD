from django.contrib import admin
from organization.models import *


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'phone_number', 'email', 'user', 'is_activated')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'location', 'phone_number', 'email', 'user', 'is_activated')
    list_editable = ('is_activated',)
    list_filter = ('time_create', 'is_activated')
    prepopulated_fields = {"slug": ("name",)}


class OrganizationCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(OrganizationCategory, OrganizationCategoryAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationPost)
