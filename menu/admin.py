from django.contrib import admin
from .models import Category, Food

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=('id','food_name','category','price','is_available')
    list_filter=('category','is_available')
    search_fields=('food_name',)
    

