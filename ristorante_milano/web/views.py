from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from decouple import config

def home(request):
    return render(request, "home.html")
