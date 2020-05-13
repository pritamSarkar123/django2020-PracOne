from django.contrib import admin
from django.urls import path, include
from first_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('second/', include('second_app.urls')),
    path('form_name/', include('basicapp.urls')),
    path('baseAppOne/', include('baseAppOne.urls')),
    path('baseAppTwo/', include('baseAppTwo.urls')),
]
