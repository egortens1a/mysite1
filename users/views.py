from django.shortcuts import render

# Create your views here.
'''path('login/', views.catalog, name='login'),
    path('registration/', views.catalog, name='registration'),
    path('profile/', views.catalog, name='profile'),
    path('logout/', views.catalog, name='logout'),'''

def login(request):
    context = {
        'title': 'Авторизация'
    }

    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Регистрация'
    }

    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'Л-Кабинет'
    }

    return render(request, 'users/profile.html', context)

def logout(request):
    context = {
        'title': 'ээ...'
    }

    return render(request, '', context)