from django.shortcuts import render
from .models import Conquista

def index(request):
    # Pega todos os itens do banco
    # Se quiser inverter a ordem (mais recente primeiro), use order_by('-ano')
    conquistas = Conquista.objects.all().order_by('ano') 
    
    context = {
        'conquistas': conquistas
    }
    return render(request, 'conquistas/index.html', context)