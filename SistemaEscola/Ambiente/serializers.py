from django.db.models import fields
from rest_framework import serializers
from .models import Ambiente

class AmbienteSerializer(serializers.Serializer):
    class Meta:
        model = Ambiente
        fields = '__all__'
