from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .mypaginations import (MyPageNumberPaginationProfessor,
                            MyPageNumberPaginationDisciplinar,
                            MyPageNumberPaginationAmbiente)
from .models import Professor, Disciplinar, Ambiente
from .serializers import (AmbienteSerializer,
                          ProfessorSerializer,
                          DisciplinaSerializer)
from rest_framework_simplejwt.views import TokenObtainPairView


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
    pagination_class = MyPageNumberPaginationProfessor

class Disciplina(ListAPIView):
    queryset = Disciplinar.objects.all()
    serializer_class = DisciplinaSerializer
    pagination_class = MyPageNumberPaginationDisciplinar

class Ambiente(ListAPIView):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    pagination_class = MyPageNumberPaginationAmbiente

class ListView()

