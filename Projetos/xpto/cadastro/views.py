from django.shortcuts import render

# Create your views here.
def cadastro(request):
    titulo = "Alunos matriculados"
    alunos = [
        {'nome': 'Maria Alves', 'curso': 'Programação em Python', 'turma': '2026.1'},
        {'nome': 'Jose Silva', 'curso': 'Inteligencia Artificial', 'turma': '2026.2'},
        {'nome': 'Marcelo Araujo', 'curso': 'Inteligencia Artificial', 'turma': '2026.2'},
        {'nome': 'Altineu Borges', 'curso': 'Programação em Python', 'turma': '2026.1'},
    ]
    return render(request, 'cadastro/alunos.html', {'dados_alunos':alunos})
