from django.shortcuts import render, get_object_or_404
from .models import Quiz

def index(request):
    return render(request, 'main/index.html')

def tours(request):
    quiz = Quiz.objects.all()
    context = {
        'quiz': quiz
    }
    return render(request, 'main/quiz.html', context)

def tour_detail(request,):
    return render(request, 'main/quiz_detail.html')

