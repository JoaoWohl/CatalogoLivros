# Catálogo de Livros 📖

<p>Projeto backend desenvolvido com o objetivo de praticar a criação de APIs REST utilizando Django, aplicando conceitos de CRUD, integração com PostgreSQL e versionamento de código com Git, por meio de um sistema de catálogo de livros.</p>

## Descrição 📝

Este projeto consiste em uma API backend para gerenciamento de um catálogo de livros, permitindo o cadastro, consulta, atualização e remoção de registros.

A aplicação foi desenvolvida utilizando Django, com persistência de dados em PostgreSQL, seguindo o padrão API REST e boas práticas de organização de código.
O versionamento do projeto foi realizado com Git, garantindo controle e histórico das alterações durante o desenvolvimento.

## Técnologias Utilizadas 🖥️

### Principais:

<div style="display:flex; gap: 20px;">
<img width="60" title="Python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
<img width="60" title="Django" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain-wordmark.svg" />
<img width="60" title="html5" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" />
<img width="60" title="css3" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" />
</div>

### Auxiliares:

<div style="display:flex; gap: 20px;">
<img width="60" title="PostgreSQL" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" />
<img width="60" title="Git" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" />
<img width="60" title="GitHub" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" />
</div>

## Como Rodar Localmente ⚙️

### Pré-requisitos

- Python 3.x
- PostgreSQL
- Git

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados PostgreSQL no arquivo settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catalogo_livros',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

Crie o banco no PostgreSQL antes:

```sql
CREATE DATABASE catalogo_livros;
```

5. Aplique as migrações:

```bash
python manage.py migrate
```

6. (Opcional) Crie um SuperUser:

```bash
python manage.py createsuperuser
```

7. Inicie o servidor:

```bash
python manage.py runserver
```
