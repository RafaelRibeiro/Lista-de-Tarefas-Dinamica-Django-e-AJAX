from django.contrib import admin          # Importa as funcionalidades do Django Admin
from myapp.models import Status, TodoList # Importa os modelos que você criou no models.py

# Registra o modelo Status no painel administrativo do Django.
# Isso permite criar, editar, listar e excluir registros de Status pelo admin.
admin.site.register(Status)

# Registra o modelo TodoList no painel administrativo do Django.
# Assim, tarefas (TodoList) podem ser gerenciadas diretamente pelo admin.
admin.site.register(TodoList)
