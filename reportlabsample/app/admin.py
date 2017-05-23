from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('identity_card', 'first_name', 'last_name', 'address', 'phone')
    search_fields = ('identity_card', 'first_name', 'last_name')

admin.site.register(Customer, CustomerAdmin)
