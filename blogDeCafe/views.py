from django.shortcuts import render
from blogDeCafe.models import Entrada, Curso

# Create your views here.
def index(request):
    entradas = Entrada.objects.all()
    cursos = Curso.objects.all().order_by("fecha")
    ctx = {"entradas": entradas, "cursos": cursos}
    return render(request, "index.html", ctx)

def nosotros(request):
    return render(request, "nosotros.html")

def cursos(request):
    cursos = Curso.objects.all().order_by("fecha")
    ctx = {"cursos": cursos}
    return render(request, "cursos.html", ctx)

def contacto(request):
    return render(request, "contacto.html")

def blog(request, id):
    entrada = Entrada.objects.filter(id=id)
    if len(entrada) == 1:
        entrada = entrada[0]
        ctx = {"entrada": entrada}
        entrada.contenido = entrada.contenido.split("\n")
        return render(request, "blog.html", ctx)
    else:
        return render(request, "La entrada está caída")
