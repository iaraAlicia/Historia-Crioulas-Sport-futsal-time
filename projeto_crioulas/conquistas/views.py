from django.shortcuts import render, redirect
from .models import Conquista
from .forms import ConquistaForm
from django.contrib.auth.decorators import login_required # Importante para segurança

# A view pública (que já existia)
def index(request):
    conquistas = Conquista.objects.all().order_by('ano')
    context = {'conquistas': conquistas}
    return render(request, 'conquistas/index.html', context)

# --- NOVA VIEW DO PAINEL ---
@login_required # Só deixa entrar se estiver logado
def painel(request):
    # Lógica para salvar o formulário
    if request.method == 'POST':
        form = ConquistaForm(request.POST, request.FILES) # request.FILES é obrigatório para imagens
        if form.is_valid():
            form.save()
            return redirect('conquistas:painel') # Recarrega a página limpa
    else:
        form = ConquistaForm()

    # Lista para mostrar no painel
    conquistas = Conquista.objects.all().order_by('-ano') # Do mais novo pro mais antigo
    
    return render(request, 'conquistas/painel.html', {'form': form, 'conquistas': conquistas})

# View para deletar (Opcional, mas útil)
@login_required
def deletar_conquista(request, id):
    item = Conquista.objects.get(id=id)
    item.delete()
    return redirect('conquistas:painel')