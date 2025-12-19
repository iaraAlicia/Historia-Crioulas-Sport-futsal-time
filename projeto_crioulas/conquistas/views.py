from django.shortcuts import render, redirect
from .models import Conquista
from .forms import ConquistaForm
from django.contrib.auth.decorators import login_required

# 1. A Página Pública (Roleta)
def index(request):
    conquistas = Conquista.objects.all().order_by('ano')
    context = {'conquistas': conquistas}
    return render(request, 'conquistas/index.html', context)

# 2. O Painel Administrativo (Só com senha)
@login_required 
def painel(request):
    if request.method == 'POST':
        form = ConquistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('conquistas:painel') # Recarrega para limpar
    else:
        form = ConquistaForm()

    # Lista para tabela (Do mais novo pro antigo)
    conquistas_lista = Conquista.objects.all().order_by('-ano') 
    
    return render(request, 'conquistas/painel.html', {'form': form, 'conquistas': conquistas_lista})

# 3. Função de Deletar
@login_required
def deletar_conquista(request, id):
    item = Conquista.objects.get(id=id)
    item.delete()
    return redirect('conquistas:painel')