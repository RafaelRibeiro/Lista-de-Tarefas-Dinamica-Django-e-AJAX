from django.shortcuts import render, redirect, get_object_or_404  # Funções para renderizar templates, redirecionar e buscar objetos.
from django.http import JsonResponse                              # Retorna respostas JSON (útil para AJAX).
from myapp.forms import TodoListForm                              # Importa o formulário.
from myapp.models import TodoList                                 # Importa o modelo TodoList.


# View para criar itens e exibir a lista.
def create_item(request):
    todo = TodoList.objects.all()              # Busca todos os itens.

    if request.method == "POST":               # Se enviar dados via POST...
        form = TodoListForm(request.POST)      # Cria o formulário com os dados.
        if form.is_valid():                    # Valida o formulário.
            form.save()                        # Salva no banco.
            return redirect('/')               # Redireciona para "/".

    form = TodoListForm()                      # Formulário vazio para GET.
    context = {"form": form, 'todo': todo}     # Dados para enviar ao template.
    return render(request, 'index.html', context)  # Renderiza o template.


# View para deletar um item.
def delete_item(request, id):
    todo = TodoList.objects.get(id=id)         # Busca o item pelo ID.
    todo.delete()                              # Deleta o item.
    return redirect('/')                       # Redireciona para "/".

    
# View para atualizar o título do item (via AJAX).
def update_item(request):  
    data_id = request.GET.get('data_id')       # Pega o ID do item.
    title = request.GET.get('title')           # Pega o novo título.

    todo = get_object_or_404(TodoList, id=data_id)   # Busca o item ou retorna 404.
    todo.title = title                               # Atualiza o título.
    todo.save()                                      # Salva no banco.

    data = {'status': 'update-item', 'title': title} # Resposta JSON.
    return JsonResponse(data)                        # Retorna resposta para o front.
