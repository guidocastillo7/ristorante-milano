from django.shortcuts import render
from .models import Category, Dish


def menu(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }

    return render(request, "menu.html", context)


def home(request):
    return render(request, "home.html")
