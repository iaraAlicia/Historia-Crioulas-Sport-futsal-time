from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),       
    path('historia/', views.historia, name='historia'), 
    # path('galeria/', views.galeria, name='galeria'),  
    # path('conquistas/', views.conquistas, name='conquistas'),  
    # path('contato/', views.contato, name='contato'),  
]