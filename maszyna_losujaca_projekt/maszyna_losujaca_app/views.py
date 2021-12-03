from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import DrawCandidate, Draw


def drawing(candidates):
    pass


def index(request):
    candidates = DrawCandidate.objects.all()
    if Draw.objects.count() == 0:
        return render(request, 'maszyna_losujaca_app/index.html', {'candidates': candidates})
    else:
        return render(request, 'maszyna_losujaca_app/index_after_draw.html', {'candidates': candidates})


def join(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name != "" and password != "":
            DrawCandidate.objects.create(name=name, password=password)
            return render(request, 'maszyna_losujaca_app/joined.html', {})
        else:
            return redirect("index")
    elif request.method == "GET":
        return render(request, 'maszyna_losujaca_app/join.html', {})


def draw(request):
    if request.method == "POST":
        if request.POST.get('password') == 'dupa':
            Draw.objects.create(name='Mikołajki')
            drawing(DrawCandidate.objects.all())
            return redirect('index')
    return render(request, 'maszyna_losujaca_app/draw.html', {})


def check_result(request):
    if request.method == "POST":
        chosen_candidate = "wylosowana osoba"
        return render(request, 'maszyna_losujaca_app/result.html', {'candidate': chosen_candidate})
    elif request.method == "GET":
        return render(request, 'maszyna_losujaca_app/check_result.html', {})
