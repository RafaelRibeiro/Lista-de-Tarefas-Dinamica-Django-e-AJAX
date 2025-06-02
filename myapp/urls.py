from django.urls import path  # Importa path para criar rotas.
from myapp import views       # Importa as views da aplicação.

# Definição das rotas (URLs) da aplicação.
urlpatterns = [
    path('', views.create_item, name='create_item'),                   # Rota principal ("/") — cria novos itens e lista todos.
    path('delete/<int:id>/', views.delete_item, name='delete'),        # Rota para deletar um item específico pelo ID (ex: /delete/5/)
    path('update-item/', views.update_item, name='update-item'),       # Rota para atualizar o título do item via AJAX (ex: /update-item)
    path('update-status/', views.update_status, name='update-status'), # Rota para atualizar o status do item via AJAX (ex: /update-status)
]
