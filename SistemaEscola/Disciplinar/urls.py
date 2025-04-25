from django.urls import path
from . import views

urlpatterns = [
    path('', views.OverviewAPI, name='Disciplinares'),
    path('disciplina/cadastrar', views.cadastrar, name="Cadastro"),
    path('disciplina/', views.leitura, name='Leitura'),
    path('disciplina/<int:pk>', views.leituraPK, name='Leitura com PK'),
    path('disciplina/atualizar/<int:pk>', views.atualizar, name='Atualização'),
    path('disciplina/deletar/<int:pk>', views.deletar, name='Exclusão')
]