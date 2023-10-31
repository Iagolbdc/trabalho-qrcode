from rest_framework import serializers
from .models import *

class AlunoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Aluno
        fields = '__all__'

class UpdateAlunoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aluno
        fields = '__all__'
        read_only_fields = ['qrcode']

    nome = serializers.CharField(required=False)
    sobrenome = serializers.CharField(required=False)
    idade = serializers.IntegerField(required=False)
    foto = serializers.ImageField(required=False)
