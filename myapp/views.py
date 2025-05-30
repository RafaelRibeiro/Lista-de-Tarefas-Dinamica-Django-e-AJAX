from django.shortcuts import render, redirect  # Importa funções para renderizar templates e redirecionar.
from myapp.forms import TodoListForm           # Importa o formulário TodoListForm.
from myapp.models import TodoList              # Importa o modelo TodoList.


# View para criar itens e exibir a lista.
def create_item(request):
    todo = TodoList.objects.all()              # Busca todos os itens da lista.

    if request.method == "POST":               # Se o método for POST...
        form = TodoListForm(request.POST)      # Cria o formulário com os dados enviados.
        if form.is_valid():                    # Se o formulário for válido...
            form.save()                        # Salva no banco de dados.
            return redirect('/')               # Redireciona para a página inicial.

    form = TodoListForm()                      # Cria um formulário vazio (para GET).
    context = {"form": form, 'todo': todo}     # Dados que serão enviados para o template.
    return render(request, 'index.html', context)  # Renderiza o template com o contexto.


# View para deletar um item.
def delete_item(request, id):
    todo = TodoList.objects.get(id=id)         # Busca o item pelo ID.
    todo.delete()                              # Deleta o item.
    return redirect('/')                       # Redireciona para a página inicial.