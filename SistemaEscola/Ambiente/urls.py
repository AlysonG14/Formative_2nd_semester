from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.OverviewAPI, name='Ambientes'),
    path('professor', views.Professor.as_view()),
    path('disciplina', views.Disciplina.as_view()),
    path('ambiente', views.Ambiente.as_view())
]