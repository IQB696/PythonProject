from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('id')[:5]
    return render(request, 'msgr/index.html', {'title': 'Главная страница', 'tasks': tasks})


def about(request):
    return render(request, 'msgr/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error ='Сообщение не отправилось'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'msgr/create.html', context)
