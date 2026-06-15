from django.shortcuts import render
from .models import Aluno

def alunos(request):
    titulo = "Alunos e Campus"
    dados_alunos = Aluno.objects.all()

    return render(request, 'cadastro/alunos.html', {'titulo': titulo, 'alunos': dados_alunos})
