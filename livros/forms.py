from django import forms
from .models import Livro, Categoria, Autor, Editora

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class FormAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']

class FormEditora(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']

class FormLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo','autor','editora','categoria','lancamento']