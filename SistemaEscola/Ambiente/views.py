from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import status, serializers
from .models import Professor, Disciplinar, Ambiente
from .serializers import (AmbienteSerializer,
                          ProfessorSerializer,
                          DisciplinaSerializer)


# Create your views here.

@api_view(['GET'])
def OverviewAPI(request):
    api_urls = {
        "all_itens": '/',
        "Professor": '/professor',
        "Disciplina": '/disciplina',
        "Ambiente": '/ambiente',
    }
    return Response(api_urls)

class Professor(ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class Disciplina(ListAPIView):
    queryset = Disciplinar.objects.all()
    serializer_class = DisciplinaSerializer

class Ambiente(ListAPIView):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer