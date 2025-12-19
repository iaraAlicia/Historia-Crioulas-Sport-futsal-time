from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views  # Importando a view da Home

urlpatterns = [
    # 1. Admin do Django
    path('admin/', admin.site.urls),

    # 2. Login/Logout (Obrigatório para o painel)
    path('accounts/', include('django.contrib.auth.urls')),

    # 3. Home Page (Core)
    path('', views.home, name='home'),

    # 4. Apps (Usando include para ficar organizado)
    path('historia/', include('historia.urls')),
    path('conquistas/', include('conquistas.urls')), # O Painel está aqui dentro!
    path('galeria/', include('galeria.urls')),
]

# Configuração para imagens funcionarem
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)