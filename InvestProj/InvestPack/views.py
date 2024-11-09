#В этом файле объявляются переменные, хранящие ссылки на страницы
#Формирует http ответ - html страницу
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("СТРАНИЦА ПРИЛОЖЕНИЯ")

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


