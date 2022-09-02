from django.shortcuts import render, redirect
from .models import Sms
from .forms import SmsForm


def index(request):
    smska = Sms.objects.order_by('id')[:5]
    return render(request, 'msgr/index.html', {'title': 'Main page', 'tasks': smska})


def about(request):
    return render(request, 'msgr/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = SmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            error ='Error send'
        else:
            error ='Error send'

    form = SmsForm()
    context = {
        'form': form
    }
    return render(request, 'msgr/create.html', context)
