from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from app1 import views

urlpatterns = [
    path('', views.index),
]