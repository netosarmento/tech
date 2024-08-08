from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

def home_page(request):
    
    return render(request, 'index.html')

def servicos(request):
    
    return render(request, 'servicos.html')

def contatos(request):
    
    return render(request, 'contato.html')

def sobre(request):
    
    return render(request, 'sobre.html')

def ceo(request):
    
    return render(request, 'ceo.html')