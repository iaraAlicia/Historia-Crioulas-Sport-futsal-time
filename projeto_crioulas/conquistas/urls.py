from django.urls import path
from . import views

app_name = 'conquistas'

urlpatterns = [
    path('', views.index, name='index'),
    path('painel/', views.painel, name='painel'),
    path('deletar/<int:id>/', views.deletar_conquista, name='deletar'),
]