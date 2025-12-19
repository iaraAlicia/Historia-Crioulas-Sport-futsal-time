from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    # Mesmo sem banco de dados, se quiser passar dados dinâmicos no futuro,
    # você faria isso aqui (ex: lista de titulos).
    # Por enquanto, só renderiza o template base.
    return render(request, 'index.html')


def historia(request):
    return render(request, 'historia/index.html')

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')