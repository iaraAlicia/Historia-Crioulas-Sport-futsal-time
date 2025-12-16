from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    # O Django procura automaticamente em templates/historia/index.html
    return render(request, 'historia/index.html')