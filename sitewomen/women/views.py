from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from women.models import Women

# Create your views here.


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

def index(request):
    posts = Women.published.all()
    data = {
        'title': 'главная',
        'float': 1.15,
        'posts': posts,
        'menu': menu,
        }

    return render(request, 'women/index.html', data)

def about(request):
    return render(request, 'women/about.html', {'title': 'о сайте', 'menu': menu})

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'women/post.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Контакт')

def login(request):
    return HttpResponse('login')

def show_category(request, cat_id):
    posts = Women.published.all()
    data = {
        'title': 'Отображение по рубрикам',
        'posts': posts,
        'menu': menu,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)