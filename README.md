# Django Configuração de Projeto Padrão (Simples)

Curso: https://www.udemy.com/course/pythondjango-construindo-uma-lista-de-tarefas-dinamica-com-ajax

**Configurações Iniciais**

<details><summary><b>Ambiente Virtual Linux/Windows</b></summary>

- **Ambiente Virtual Linux/Windows**
    
    
    Lembrando… Precisa ter Python instalado no seu ambiente.
    
    **Criar o ambiente virtual Linux/Windows**
     
    ```python
    ## Windows
    python -m venv .venv
    source .venv/Scripts/activate # Ativar ambiente
    
    ## Linux 
    ## Caso não tenha virtualenv. "pip install virtualenv"
    virtualenv .venv
    source .venv/bin/activate # Ativar ambiente
    ```
    
    Instalar os seguintes pacotes.
    
    ```python
    pip install django
    pip install pillow
    ```
    
    Para criar o arquivo *requirements.txt*
    
    ```python
    pip freeze > requirements.txt
    ```

</details>

<details><summary><b>Criando o Projeto</b></summary>

- **Criando o Projeto**
    
    ## **Criando o projeto**
    
    “core” é nome do seu projeto e quando colocamos um “.” depois do nome do projeto significa que é para criar os arquivos na raiz da pasta. Assim não cria subpasta do projeto.
    
    ```python
    django-admin startproject core .
    ```
    
    **Testar a aplicação**
    
    ```python
    python manage.py runserver
    ```
    
</details>

<details><summary><b>Configurar Settings e Arquivos Static</b></summary>

- **Configurar Settings e Arquivos Static**
    
    ## **Vamos configurar nossos arquivos** *static*
    
    ```python
    import os 
    
    # base_dir config
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
    STATIC_DIR=os.path.join(BASE_DIR,'static')
    
    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
        }
    }
    
    STATIC_ROOT = os.path.join(BASE_DIR,'static')
    STATIC_URL = '/static/' 
    
    MEDIA_ROOT=os.path.join(BASE_DIR,'media')
    MEDIA_URL = '/media/'
    
    # Internationalization
    # Se quiser deixar em PT BR
    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'
    USE_I18N = True
    USE_L10N = True 
    USE_TZ = True
    ```
    
    *myapp/urls.py*
    
    ```python
    from django.contrib import admin
    from django.conf import settings
    from django.conf.urls.static import static
    from django.urls import path
    
    urlpatterns = [
        path('admin/', admin.site.urls),
    ]
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto
    ```
</details>

<details><summary><b>Criando Aplicativo</b></summary>

- **Criando Aplicativo**
    
    **Vamos criar nosso aplicativo no Django.**
    
    Para criar a aplicação no Django rode comando abaixo. “myapp” é nome do seu App.
    
    ```python
    python manage.py startapp myapp
    ```
    
    Agora precisamos registrar nossa aplicação no *INSTALLED_APPS* localizado em *settings.py*.
    
</details>

<details><summary><b>Template base e Bootstrap Configuração</b></summary>

- **Template base e Bootstrap Configuração**
    
    ### Bootstrap configuração
    
    Doc: [https://getbootstrap.com/docs/5.2/getting-started/introduction/](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
    
    Com Base na documentação para utilizar os recursos Boostrap basta adicionar as tags de CSS e JS. No HTML da Pagina Base.
    
    ```python
    <!-- CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    
    <!-- JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    ```
    
    ## Template Base
    
    1 - criar um arquivo base ***base.html*** onde vamos renderizar nosso conteúdo. 
    
    ```python
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
    	<meta charset="UTF-8">
    	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<title>{% block title %}{% endblock %}</title>
    
    	<!-- CSS -->
    	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    
    </head>
    <body>  
    	
    	{% block content %}
    	
    	{% endblock %} 
     
    	<!-- JS-->
    	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    </body>
    </html>
    ```

</details>

<details><summary><b>Cria uma View</b></summary>

- **Cria uma View**
    
    *index1.html*
    
    ```html
    {% extends 'base.html' %}
    {% block title %}Pagina Inicial{% endblock %}
    {% block content %}
    	<h1>Pagina Inicial</h1>
    {% endblock %}
    ```
    
    *myapp/views.py*
    
    ```python
    from django.shortcuts import render
    
    # Create your views here.
    def mysite(request):
        return render(request, 'index1.html')
    ```
    
    criar arquivo *myapp*/*urls.py*
    
    ```
    from django.urls import path 
    from myapp import views
    
    urlpatterns = [
        path('', views.mysite, name='mysite'), 
    ]
    ```
    
    urls.py do projeto. ***core/urls.py***
    
    ```python
    from django.contrib import admin
    from django.urls import path, include # adicionar include
    from django.conf import settings
    from django.conf.urls.static import static 
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('myapp.urls')), # url do app
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto
    ```
    
    Rodar o projeto para ver como está.
    
    ```python
    python manage.py makemigrations && python manage.py migrate
    python manage.py runserver
    ```
    
    .gitignore
    
    ```python
    /tmp
    passenger_wsgi.py 
    .venv
    db.sqlite3
    /static_media
    static_media
    /static_files
    static_files
    /media
    mydatabase
    file_name.sql
    __pycache__ 
    __pycache__/
    ```

</details>

- **Cria as migrations**

    **Migrations.**

    # Cria os arquivos de migração com base nas alterações feitas nos modelos.
    # Esse comando gera os scripts necessários para criar ou atualizar as tabelas no banco de dados.
        ```python
        python manage.py makemigrations
        ```

    # Executa as migrações no banco de dados, aplicando as mudanças definidas no passo anterior.
    # Cria as tabelas, campos e relações conforme os modelos do projeto.
        ```python
        python manage.py migrate
        ```

    # Cria um superusuário (administrador) para acessar o painel de administração do Django.
    # Durante a execução, será solicitado um nome de usuário, e-mail e senha.
        ```python
        python manage.py createsuperuser
        ```

</details>

- **Status**
        
    - **Adição de Status**
            # Define os diferentes estados que uma tarefa pode assumir:
            # ⛔️ A Fazer
            # ⚠️ Fazendo
            # ✅ Finalizado
    
</details>
