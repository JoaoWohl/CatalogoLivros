from django.db import models
from datetime import date

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=160)

    class Meta:
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome
    

class Editora(models.Model):
    nome = models.CharField(max_length=64)
    
    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=128)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, default="")
    lancamento = models.DateField(default=date.today)

    def __str__(self):
        return self.titulo
