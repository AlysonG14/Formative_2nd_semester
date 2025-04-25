from django.urls import path
from . import views

urlpatterns = [
    path('', views.OverviewAPI, name='Ambientes'),
    path('ambiente/cadastrar', views.cadastar, name='Cadastrar'),
    path('ambiente/', views.leitura, name='Leitura'),
    path('ambiente/<int:pk>', views.leituraPK, name='Leitura com PK'),
    path('ambiente/deletar', views.deletar, name='Deletar')
]