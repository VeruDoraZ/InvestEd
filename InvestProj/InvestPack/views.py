#В этом файле объявляются переменные, хранящие ссылки на страницы
#Формирует http ответ - html страницу
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *


menu = ["О сайте", "Добавить проект", "Обратная связь", "Войти", "Шаблон"]

def index(request):
    posts = startupCard.objects.all()
    return render(request, 'InvestPack/index.html', {'posts':  posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'InvestPack/about.html', {'menu': menu, 'title': 'О сайте'})

def base(request):
    return render(request, 'InvestPack/base.html', {'menu': menu, 'title': 'Шаблон'})


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")
#archive возвращает пользователя на начальный экран(ф-ия redirect)
def archive(request, year):
    if int(year) > 2024:
       return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


