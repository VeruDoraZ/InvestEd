from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('quizzes/', views.tours, name='quiz'),
    path('quizzes/', views.tour_detail, name='quiz_detail'),
]