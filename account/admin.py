from django.contrib import admin

from account.models import *

class AccountPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug')
    list_display_links = ('user', 'slug')
    search_fields = ('user', 'slug')
    list_filter = ('user', 'slug')

admin.site.register(CustomUser)
admin.site.register(AccountPost, AccountPostAdmin)
