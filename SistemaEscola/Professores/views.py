from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from django.shortcuts import render, get_object_or_404
from .models import Professor
from .serializers import ProfessorSerializer

# Create your views here.

@api_view(['GET'])
def OverviewAPI(request):
    api_urls = {
        "all_itens": '/',
        "Cadastro": 'professor/cadastrar',
        "Leitura": 'professor/',
        "Leitura com PK": 'professor/<int:pk>',
        "Atualizar": 'professor/atualizar/<int:pk>',
        "Deletar": 'professor/deletar/<int:pk>'
    }
    return Response(api_urls)

@api_view(['POST'])
def cadastrar(request):
    professor = ProfessorSerializer(data=request.data)
    if Professor.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Erro! Esse tipo de informação ainda existe!')
    if professor.is_valid():
        professor.save()
        return Response(professor.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def leitura(request):
    if request.query_params:
        professor = Professor.objects.filter(**request.query_params.dict())
    else:
        professor = Professor.objects.all()
    if professor:
        serializer = ProfessorSerializer(professor, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def leituraPK(request, pk):
    try:
        professor = Professor.objects.get(pk=pk)
    except Professor.DoesNotExist:
        return Response("{'Erro': 'Professor não encontrado'}", status=status.HTTP_404_NOT_FOUND)
    serializer = ProfessorSerializer(professor)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def atualizar(request, pk):
    professor = Professor.objects.all(pk=pk)
    data = ProfessorSerializer(isinstance=professor, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def deletar(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    professor.delete()
    return Response(status=status.HTTP_201_CREATED)




