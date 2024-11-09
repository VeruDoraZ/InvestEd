from django.urls import path, include, re_path
from django.utils import archive

from .views import *
#Закидываем все url адреса сюда
urlpatterns = [
    path('', index, name = 'home'),
    path('cats/<int:catid>/', categories),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive),
]
