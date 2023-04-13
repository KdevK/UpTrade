from django.contrib import admin
from django.urls import path, re_path
from web.views import menu

urlpatterns = [
    re_path(r'^', menu, name='menu'),
]