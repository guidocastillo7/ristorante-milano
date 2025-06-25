from django.contrib import admin
from .models import Category, Dish

admin.site.register(Category)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price"
    )
