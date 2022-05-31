from django.contrib import admin

from subscription.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriper', 'user', 'master')
    list_display_links = ('subscriper', 'user', 'master')
    search_fields = ('subscriper', 'user', 'master')
    list_filter = ('subscriper', 'user', 'master')


admin.site.register(Subscription, SubscriptionAdmin)
