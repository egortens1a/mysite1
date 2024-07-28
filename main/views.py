from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница - HOME'
    }

    return render(request, 'main\index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Что ты хотел здесь увидеть?'
    }

    return render(request, r"main\about.html", context)