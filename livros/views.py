from django.shortcuts import render, redirect
from .models import Livro, Autor, Categoria, Editora
from .forms import FormAutor, FormEditora, FormCategoria, FormLivro


def home(request):
    data = {
        "Livros": Livro.objects.all(),
        }

    return render(request, 'livros/home.html', data)

def editCatalogo(request):
    data = {
        'Livros': Livro.objects.all(),
    }

    return render(request, 'livros/editCatalogo.html', data)

def addLivro(request):
    data = {}

    data['form'] = FormLivro(request.POST or None)
    
    if data['form'].is_valid():
        data['form'].save()
        return redirect('editCatalogo')

    return render(request, 'livros/addLivro.html', data)

def editLivro(request, id):
    data = {}

    livro = Livro.objects.get(id=id)
    
    data['form'] = FormLivro(request.POST or None, instance=livro)

    if data['form'].is_valid():
        data['form'].save()
        return redirect('editCatalogo')
    
    return render(request, 'livros/editLivro.html', data)

def deleteLivro(request, id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect('editCatalogo')

def addAutor(request):
    data = {}

    data['autores'] = Autor.objects.all()

    data['form'] = FormAutor(request.POST or None)

    if data['form'].is_valid():
        data['form'].save()
        return redirect('addAutor')
    
    return render(request, 'livros/Autor.html', data)

def deleteAutor(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect('addAutor')

def addEditora(request):
    data = {}
    data['editoras'] = Editora.objects.all()
    data['form'] = FormEditora(request.POST or None)

    if data['form'].is_valid():
        data['form'].save()
        return redirect('addEditora')
    
    return render(request, 'livros/addEditora.html', data)

def deleteEditora(request, id):
    editora = Editora.objects.get(id=id)
    editora.delete()
    return redirect('addEditora')

def addCategoria(request):
    data = {}
    data['categorias']= Categoria.objects.all()
    data['form']= FormCategoria(request.POST or None)

    if data['form'].is_valid():
        data['form'].save()
        return redirect('addCategoria')
    
    return render(request, 'livros/addCategoria.html',data)

def deleteCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('addCategoria')