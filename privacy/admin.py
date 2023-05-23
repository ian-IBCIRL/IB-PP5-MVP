from django.contrib import admin
from .models import Privacy


@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['title', ]
