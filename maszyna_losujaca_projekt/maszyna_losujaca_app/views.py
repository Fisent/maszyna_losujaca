from django.http import HttpResponse
from django.shortcuts import render

from .models import DrawCandidate


def index(request):
    return render(request, 'maszyna_losujaca_app/index.html', {})


def join(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        DrawCandidate.objects.create(name=name, password=password)
        return render(request, 'maszyna_losujaca_app/joined.html', {})
    elif request.method == "GET":
        return render(request, 'maszyna_losujaca_app/join.html', {})


