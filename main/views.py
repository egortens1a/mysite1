from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.
def index(request):

    categories = Categories.objects.all()
    context = {
        'title': 'Home',
        'content': 'Главная страница - HOME',
        'categories': categories
    }

    return render(request, 'main\index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Что ты хотел здесь увидеть?'
    }

    return render(request, r"main\about.html", context)