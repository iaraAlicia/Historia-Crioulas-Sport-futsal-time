from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),       
    path('historia/', views.historia, name='historia'), 
<<<<<<< Updated upstream
    # path('galeria/', views.galeria, name='galeria'),  
    # path('conquistas/', views.conquistas, name='conquistas'),  
    # path('contato/', views.contato, name='contato'),  
=======
    path('galeria/', views.galeria, name='galeria'),  
    path('conquistas/', views.conquistas, name='conquistas'),  
    path('contato/', views.contato, name='contato'),  
    path('painel/', views.painel, name='painel'), # Painel Admin
    path('deletar/<int:id>/', views.deletar_conquista, name='deletar'), # Rota para apagar
>>>>>>> Stashed changes
]