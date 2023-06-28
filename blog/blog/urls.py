
from django.contrib import admin
from django.urls import path
from .views import index, contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto')
]
