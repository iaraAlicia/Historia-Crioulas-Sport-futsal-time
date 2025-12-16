from django.urls import path
from . import views

# Isso permite usar {% url 'historia:index' %} nos templates
app_name = 'historia'

urlpatterns = [
    path('', views.index, name='index'),
]