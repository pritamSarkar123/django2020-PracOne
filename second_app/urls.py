from django.urls import path
from . import views
urlpatterns = [
    path('', views.help, name='second'),
    path('home/', views.home, name='home')
]
