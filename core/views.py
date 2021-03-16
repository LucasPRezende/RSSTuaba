from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def leitor(request):
    return render(request, "leitor.html")

def registrar(request):
    return render(request, "registrar.html")