from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'maszyna_losujaca_app/index.html', {})
