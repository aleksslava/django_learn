from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string


# Create your views here.
data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    data = {
        'title': 'главная',
        'float': 1.15,
        'posts': data_db,
        'menu': menu,
    }

    return render(request, 'women/index.html', data)

def about(request):
    return render(request, 'women/about.html', {'title': 'о сайте', 'menu': menu})

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи {post_id}')

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Контакт')

def login(request):
    return HttpResponse('login')