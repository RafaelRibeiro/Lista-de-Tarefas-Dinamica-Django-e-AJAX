from django.urls import path  # Importa a função path para definir rotas.
from myapp import views       # Importa as views que serão usadas nas rotas.

# Lista de URLs da aplicação.
urlpatterns = [
    path('', views.create_item, name='create_item'),            # Rota principal ("/") que chama a view create_item.
    path('delete/<int:id>/', views.delete_item, name='delete'), # Rota para deletar item pelo ID.
]