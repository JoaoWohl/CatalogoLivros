from django.shortcuts import render
from .models import Livro


def home(request):
    data = {
        "Livros": Livro.objects.all()
        }

    return render(request, 'livros/home.html', data)

def editCatalogo(request):
    data = {
        'Livros': Livro.objects.all()
    }

    return render(request, 'livros/editCatalogo.html', data)

def addLivro(request):
    data = {

    }
    return render(request, addLivro, data)