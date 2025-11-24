from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print("Функция home вызвана!")  # Это покажется в консоли
    return render(request, 'static_handler.html')

def hello(request):
    return HttpResponse('Привет, Мир! (страница hello)')