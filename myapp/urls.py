from django.urls import path  # Importa path para criar rotas.
from myapp import views       # Importa as views da aplicação.

# Definição das rotas (URLs) da aplicação.
urlpatterns = [
    path('', views.create_item, name='create_item'),            # Rota principal ("/") — criar e listar itens.
    path('delete/<int:id>/', views.delete_item, name='delete'), # Rota para deletar item pelo ID.
    path('update/', views.update_item, name='update-item'),     # Rota para atualizar título ou status via AJAX.
]