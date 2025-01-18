from django.http import HttpResponse

from django.shortcuts import render
from .forms import UserRegister


# Create your views here.

def sign_up_by_django(request):
    users = ['Alek', 'Elena', 'Oleg']
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            for user in users:
                if user == username:
                    return HttpResponse('Пользователь уже существует')
            if password != repeat_password:
                return HttpResponse('Пароли не совпадают')
            if int(age) < 18:
                return HttpResponse('Вы должны быть старше 18')
            return HttpResponse('Вы успешно зарегистрировались!')
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})

def sign_up_by_html(request):
    users = ['Alek', 'Elena', 'Oleg']
    if request.method == 'POST':
        form = UserRegister(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        for user in users:
            if user == username:
                return HttpResponse('Пользователь уже существует')
        if password != repeat_password:
            return HttpResponse('Пароли не совпадают')
        if int(age) < 18:
            return HttpResponse('Вы должны быть старше 18')
        return HttpResponse('Вы успешно зарегистрировались!')
    return render(request, 'fifth_task/registration_page.html')