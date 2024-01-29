from django.contrib import admin

from staff.models import ChefModel


@admin.register(ChefModel)
class CHefModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession', 'info']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']



