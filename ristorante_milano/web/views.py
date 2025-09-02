from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from decouple import config

def home(request):
    return render(request, "home.html")


def create_superuser(request):
    username = "admin"
    password = "123456789"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username,
                                      password=password)

    return redirect("/")
