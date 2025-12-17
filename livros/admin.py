from django.contrib import admin
from .models import Categoria, Autor, Livro, Editora


# Register your models here.

admin.site.register([Categoria, Autor, Livro, Editora])