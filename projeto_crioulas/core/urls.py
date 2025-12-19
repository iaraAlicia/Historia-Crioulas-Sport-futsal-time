from django.urls import path
from . import views

urlpatterns = [
    # Apenas a Home fica aqui.
    # As outras (historia, conquistas) já estão no arquivo principal do projeto.
    path('', views.home, name='home'),
]