from django.shortcuts import render, redirect
from .models import Sms
from .forms import SmsForm


def index(request):
    smska = Sms.objects.order_by('id')[:5]
    return render(request, 'msgr/index.html', {'title': 'Main page', 'tasks': smska})


def about(request):
    return render(request, 'msgr/about.html')


def __validate(form, str):
    x = ('0', '1', '2')
    for c in str:
        if x.__contains__(c):
            form.add_error('title', 'ERROR')


def create(request):
    error = ''
    if request.method == 'POST':
        form = SmsForm(request.POST)
        __validate(form, form.data.get('title'))
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error ='Error send'

    form = SmsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'msgr/create.html', context)
