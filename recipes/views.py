from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # context permite passar variaveis para o html
    return render(request, 'recipes/home.html', context={'name': 'Lucas Campos'})


def sobre(request):
    return HttpResponse('SOBRE')
