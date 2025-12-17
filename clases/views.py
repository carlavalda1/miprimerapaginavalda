from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'clases/index.html')

def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "clases/cursos.html", contexto)