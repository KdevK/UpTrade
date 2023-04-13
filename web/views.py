from django.shortcuts import render
from web.models import Category


def menu(request, url=None):
    return render(request, 'index.html')
