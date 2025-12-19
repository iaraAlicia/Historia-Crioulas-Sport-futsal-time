from django.urls import path
from . import views

app_name = 'conquistas'

urlpatterns = [
    path('', views.index, name='index'), # Página pública
    path('painel/', views.painel, name='painel'), # Painel Admin
    path('deletar/<int:id>/', views.deletar_conquista, name='deletar'), # Rota para apagar
]