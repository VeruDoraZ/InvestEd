from django.urls import path, include, re_path
from django.utils import archive

from .views import *
#Закидываем все url адреса сюда
urlpatterns = [
    path('', index, name = 'home'),
    path('about/', about, name = 'about'),
    path('base/', about, name='base'),

]
