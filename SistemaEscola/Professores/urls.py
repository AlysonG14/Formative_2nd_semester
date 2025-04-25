from django.urls import path
from . import views

urlpatterns = [
    path('', views.OverviewAPI, name='Professores'),
    path('professor/cadastrar', views.cadastrar, name="Cadastro"),
    path('professor/', views.leitura, name='Leitura'),
    path('professor/<int:pk>', views.leituraPK, name='Leitura com PK'),
    path('professor/atualizar/<int:pk>', views.atualizar, name='Atualização'),
    path('professor/deletar/<int:pk>', views.deletar, name='Exclusão')
]

