from django.contrib import admin
from .models import Contact, Address


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Contact management section for admin
    """
    list_display = ['name', 'topic']


admin.site.register(Address)
