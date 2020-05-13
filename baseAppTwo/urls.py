from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'baseAppTwo'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
