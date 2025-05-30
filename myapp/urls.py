from django.urls import path  # Importa path para criar rotas.
from myapp import views       # Importa as views da aplicação.

# Definição das rotas (URLs) da aplicação.
urlpatterns = [
    path('', views.create_item, name='create_item'),                   # Rota principal ("/") — responsável por criar novos itens e listar todos os itens da lista.
    path('delete/<int:id>/', views.delete_item, name='delete'),        # Rota para deletar um item específico pelo ID. 
    path('update-item/', views.update_item, name='update-item'),       # Rota para atualizar o título de um item via requisição AJAX.
    path('update-status/', views.update_status, name='update-status'), # Rota para atualizar o status do item (ex: Pendente, Em Andamento, Finalizado) via AJAX. 
]
