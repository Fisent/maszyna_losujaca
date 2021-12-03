from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('join', views.join, name='join'),
    path('draw', views.draw, name='draw'),
    path('check_result', views.check_result, name='check_result'),
]
