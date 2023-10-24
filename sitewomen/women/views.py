from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from women.models import Women

# Create your views here.
data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.

Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

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
    data = {
        'title': 'главная',
        'float': 1.15,
        'posts': data_db,
        'menu': menu,
        'cat_selected': 0,
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
    data = {
        'title': 'Отображение по рубрикам',
        'posts': data_db,
        'menu': menu,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)