# Importações necessárias
from django.shortcuts import render, redirect, get_object_or_404  # Funções para renderizar templates, redirecionar e buscar objetos ou gerar erro 404.
from django.http import JsonResponse                              # Classe para retornar dados no formato JSON (útil para AJAX).
from myapp.forms import TodoListForm                              # Importa o formulário definido em forms.py.
from myapp.models import TodoList, Status                         # Importa os modelos TodoList e Status definidos no models.py.


# View responsável por criar novos itens na lista e exibir todos os itens existentes.
def create_item(request):
    todo = TodoList.objects.all()                     # Busca todos os registros da tabela TodoList (todos os itens cadastrados).
    status_list = Status.objects.all()                # Busca todos os registros da tabela Status (ex.: Pendente, Concluído).

    if request.method == "POST":                      # Verifica se o método da requisição é POST (quando o formulário é enviado).
        form = TodoListForm(request.POST)             # Cria uma instância do formulário preenchida com os dados enviados no POST.
        if form.is_valid():                           # Verifica se os dados do formulário são válidos.
            form.save()                               # Salva os dados no banco de dados (cria um novo item).
            return redirect('/')                      # Após salvar, redireciona o usuário para a página inicial ("/").

    else:                                             # Se a requisição for GET (ou qualquer outro método que não seja POST)...
        form = TodoListForm()                         # Cria um formulário vazio para ser exibido na tela.

    context = {                                       # Cria um dicionário com os dados que serão enviados para o template.
        "form": form,                                 # Formulário para adicionar novo item.
        'todo': todo,                                 # Lista de todos os itens cadastrados.
        'status_list': status_list                    # Lista de todos os status possíveis.
    }

    return render(request, 'index.html', context)     # Renderiza o template index.html com os dados do contexto.


# View responsável por deletar um item específico da lista.
def delete_item(request):
    todo_id  = request.GET.get('todo_id')             # Recupera o parâmetro 'todo_id' enviado via GET (identificador do item).
    todo = TodoList.objects.get(id=todo_id)           # Busca o item na tabela TodoList pelo ID.
    todo.delete()                                      # Exclui o item do banco de dados.
    data = {'status':'delete'}                         # Prepara uma resposta JSON com status de sucesso.
    return JsonResponse(data)                           # Retorna a resposta JSON para a requisição AJAX.


# View responsável por atualizar o título de um item (essa operação é feita via requisição AJAX).
def update_item(request):  
    data_id = request.GET.get('data_id')              # Recupera o ID do item que será editado, enviado na URL (parâmetro GET).
    title = request.GET.get('title')                  # Recupera o novo título enviado na URL (parâmetro GET).

    todo = get_object_or_404(TodoList, id=data_id)    # Busca o item pelo ID ou retorna erro 404 se não encontrar.
    todo.title = title                                # Atualiza o campo 'title' (título) do item com o novo valor.
    todo.save()                                       # Salva as alterações no banco de dados.

    data = {                                          # Prepara a resposta JSON.
        'status': 'update-item',                      # Retorna uma chave de status indicando sucesso na operação.
        'title': title                                # Retorna também o novo título atualizado.
    }

    return JsonResponse(data)                         # Retorna os dados no formato JSON para o frontend (JavaScript).


# View responsável por atualizar o status de um item (feito via AJAX).
def update_status(request):  
    data_id = request.GET.get('data_id')              # Recupera o ID do item que terá o status alterado.
    status_id = request.GET.get('status_id')          # Recupera o ID do novo status que será aplicado.

    status = get_object_or_404(Status, id=status_id)  # Busca o objeto Status correspondente ao ID fornecido ou retorna erro 404.
    todo = get_object_or_404(TodoList, id=data_id)    # Busca o objeto TodoList (item) correspondente ao ID fornecido ou retorna erro 404.

    todo.status = status                              # Atualiza o campo 'status' do item com o novo status selecionado.
    todo.save()                                       # Salva as alterações no banco de dados.

    data = {                                          # Prepara os dados para resposta JSON.
        'status': str(status_id)                      # Retorna o ID do novo status como confirmação.
    }

    return JsonResponse(data)                         # Retorna a resposta em formato JSON para o frontend (JavaScript).
