from django.urls import path, include
from django.contrib import admin
from core.views import inicio

urlpatterns = [
        path('', inicio, name="index")
]