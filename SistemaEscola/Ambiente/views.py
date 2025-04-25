from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, serializers
from .models import Ambiente
from .serializers import AmbienteSerializer

# Create your views here.

@api_view(['GET'])
def OverviewAPI(request):
    api_urls = {
        "all_itens": '/',
        "Cadastro": 'ambiente/cadastrar',
        "Leitura": 'ambiente/',
        "Leitura com PK": 'ambiente/<int:pk>',
        "Deletar": 'ambiente/deletar/<int:pk>'
    }
    return Response(api_urls)

@api_view(['POST'])
def cadastrar(request):


@api_view(['GET'])
def leitura(request):


@api_view(['GET'])
def leituraPK(request, pk):
    try:
        ambiente = Ambiente.objects.get(pk=pk)
    except Ambiente.DoesNotExist:
        return Response("{'Erro': 'Ambiente não encontrado'", status=status.HTTP_404_NOT_FOUND)
    serializer = AmbienteSerializer(ambiente)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deletar(request):




