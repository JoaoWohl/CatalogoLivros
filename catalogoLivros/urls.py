"""
URL configuration for catalogoLivros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from livros.views import home, editCatalogo, addLivro, editLivro, deleteLivro, addAutor, deleteAutor, addEditora, deleteEditora, addCategoria, deleteCategoria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('editCatalogo/', editCatalogo, name='editCatalogo'),
    path('addLivro/', addLivro, name='addLivro'),
    path('editLivro/<int:id>/', editLivro, name='editLivro'),
    path('deleteLivro/<int:id>/', deleteLivro, name='deleteLivro'),
    path('addAutor/', addAutor, name='addAutor'),
    path('deleteAutor/<int:id>/', deleteAutor, name='deleteAutor'),
    path('addEditora/', addEditora, name='addEditora'),
    path('addEditora/<int:id>/', deleteEditora, name='deleteEditora'),
    path('addCategoria/', addCategoria, name='addCategoria'),
    path('deleteCategoria/<int:id>/', deleteCategoria, name='deleteCategoria'),
]
