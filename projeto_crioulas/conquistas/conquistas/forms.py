from django import forms
from .models import Conquista

class ConquistaForm(forms.ModelForm):
    class Meta:
        model = Conquista
        fields = ['ano', 'titulo', 'descricao', 'imagem']
        
        # Estilizando os inputs para ficarem escuros (Bootstrap style manual)
        widgets = {
            'ano': forms.NumberInput(attrs={'class': 'form-control dark-input', 'placeholder': 'Ex: 2024'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control dark-input', 'placeholder': 'Título da Conquista'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control dark-input', 'rows': 3}),
            'imagem': forms.FileInput(attrs={'class': 'form-control dark-input'}),
        }