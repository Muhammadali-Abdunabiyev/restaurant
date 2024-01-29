from django.contrib import admin
from pages.models import *

@admin.register(EventModel)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'start_time', 'end_time']
    search_fields = ['location_name']
    list_filter = ['start_time', 'end_time']




@admin.register(CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'job']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(EmailModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
    list_filter = ['created_at']


@admin.register(BookTableModels)
class BookTableAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'no_of_people']
    search_fields = ['name']



