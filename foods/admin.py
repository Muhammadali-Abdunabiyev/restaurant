from django.contrib import admin
from foods.models import FoodsModel, EatModel


@admin.register(FoodsModel)
class FoodsModel(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']



@admin.register(EatModel)
class EatModel(admin.ModelAdmin):
    list_display = ['name', 'image']





