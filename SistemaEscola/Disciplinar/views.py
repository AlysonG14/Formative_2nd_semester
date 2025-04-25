from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from django.shortcuts import render, get_object_or_404
from .models import Disciplinar
from .serializers import DisciplinarSerializer

# Create your views here.

@api_view(['GET'])
def OverviewAPI(request):
    api_urls = {
        "all_itens": '/',
        "Cadastro": 'disciplina/cadastrar',
        "Leitura": 'disciplina/',
        "Leitura com PK": 'disciplina/<int:pk>',
        "Atualizar": 'disciplina/atualizar/<int:pk>',
        "Deletar": 'disciplina/deletar/<int:pk>'
    }
    return Response(api_urls)

@api_view(['POST'])
def cadastrar(request):
    disciplinar = Disciplinar(data=request.data)
    if Disciplinar.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Essa informação existe!')
    if disciplinar.is_valid():
        disciplinar.save()
        return Response(disciplinar.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def leitura(request):
    if request.query_params:
        disciplinar = Disciplinar.objects.filter(**request.query_params.dict())
    else:
        disciplinar = Disciplinar.objects.all()
    if disciplinar:
        serializer = DisciplinarSerializer(disciplinar, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def leituraPK(request, pk):
    try:
        disciplinar = Disciplinar.objects.get(pk=pk)
    except Disciplinar.DoesNotExist:
        return Response('{"Erro": "Disciplina não econtrada"}', status=status.HTTP_404_NOT_FOUND)
    serializer = DisciplinarSerializer(disciplinar)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def atualizar(request, pk):
    disciplinar = Disciplinar.objects.get(pk=pk)
    data = DisciplinarSerializer(isinstance=disciplinar, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view('DELETE')
def deletar(request, pk):
    disciplinar = get_object_or_404(Disciplinar, pk=pk)
    disciplinar.delete()
    return Response(status=status.HTTP_200_OK)

