from django.db.models import fields
from rest_framework import serializers
from .models import Disciplinar

class DisciplinarSerializer(serializers.Serializer):
    class Meta:
        model = Disciplinar
        fields = '__all__'