from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.urls import reverse
from django.core import serializers
from .serializers import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import generics, status

# Create your views here.

class CadastrarAluno(generics.GenericAPIView):
    serializer_class = AlunoSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class()
        return render(request, 'cadastroaluno.html', {'serializer': serializer})
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return redirect('listar')

class ListarAlunos(generics.GenericAPIView):
     queryset = Aluno.objects.all

     serializer_class = AlunoSerializer

     def get(self, request, *args, **kwargs):
          alunos = self.get_queryset()
          return render(request, 'listaralunos.html', {'alunos':alunos})
     
     def post(self, request, *args, **kwargs):
          serializer = self.serializer_class(data=request.data)
          return redirect('listar')

class ListaAluno(generics.GenericAPIView):
     queryset = Aluno.objects.all
     serializer_class = AlunoSerializer

     def get(self, request, *args, **kwargs):
          aluno_id = kwargs.get('pk')
          aluno = get_object_or_404(Aluno, pk=aluno_id)
          serializer = self.serializer_class(instance=aluno)

          return render(request, 'listaaluno.html', {'serializer':serializer, 'aluno': aluno})
     
class UpdateAluno(generics.GenericAPIView):
     
     queryset = Aluno.objects.all
     serializer_class = UpdateAlunoSerializer

     def get(self, request, *args, **kwargs):
        aluno_id = kwargs.get('pk')
        aluno = get_object_or_404(Aluno, pk=aluno_id)
        serializer = self.serializer_class(instance=aluno)

        return render(request, 'updatealuno.html', {'serializer':serializer, 'aluno':aluno})
     

     def post(self, request, *args, **kwargs):
        aluno_id = kwargs.get('pk')
        aluno = get_object_or_404(Aluno, pk=aluno_id)
        serializer = UpdateAlunoSerializer(instance=aluno, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return redirect('listar')
        return render(request, 'updatealuno.html', {'serializer':serializer, 'aluno':aluno})


class DeleteAluno(generics.GenericAPIView):
     
     queryset = Aluno.objects.all()
     serializer_class = AlunoSerializer

     def get(self, request, *args, **kwargs ):
          aluno_id = kwargs.get('pk')
          aluno = get_object_or_404(Aluno, pk=aluno_id)
          serializer = self.serializer_class(instance=aluno)
          return render(request, 'listaralunos.html', {'serializer': serializer, 'aluno': aluno} )
     
     def post(self, request, *args, **kwargs):
          aluno_id = kwargs.get('pk')
          aluno = get_object_or_404(Aluno, pk=aluno_id)
          aluno.delete()
          return redirect('listar')