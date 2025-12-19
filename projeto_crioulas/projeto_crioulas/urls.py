from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views  # Importando a view do Core

urlpatterns = [
    # 1. Admin
    path('admin/', admin.site.urls),

    # 2. Contas (Login)
    path('accounts/', include('django.contrib.auth.urls')),

    # 3. Home Page (Aqui estava o erro: mudamos de views.index para views.home)
    path('', views.home, name='home'),

    # 4. Apps
    path('historia/', include('historia.urls')),
    path('conquistas/', include('conquistas.urls')),
    path('galeria/', include('galeria.urls')),
]

# Configuração de Mídia (Imagens)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)