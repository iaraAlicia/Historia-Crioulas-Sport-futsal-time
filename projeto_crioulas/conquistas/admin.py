from django.contrib import admin
from .models import Conquista

@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    list_display = ('ano', 'titulo') # O que aparece na lista
    search_fields = ('titulo', 'ano')