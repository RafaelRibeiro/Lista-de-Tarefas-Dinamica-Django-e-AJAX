from django.db import models # Importa o módulo de models do Django, que permite a criação de modelos ORM.

# Modelo que representa um status para tarefas (ex.: "Pendente", "Em andamento", "Concluído").
class Status(models.Model):
    name = models.CharField(max_length=25) # Campo de texto para o nome do status, limitado a 25 caracteres.

    # Representação legível do objeto (útil no admin e no shell).
    def __str__(self):
        return self.name
    
    # Status:
    # Define os diferentes estados que uma tarefa pode assumir:
    # ⛔️ A Fazer
    # ⚠️ Fazendo
    # ✅ Finalizado

# Modelo que representa uma tarefa ou item de uma lista.
class TodoList(models.Model):
    title = models.CharField(max_length=100) # Título da tarefa, limitado a 100 caracteres.

# Relacionamento com o modelo Status.
    status = models.ForeignKey(
        Status,                   # Modelo de destino (tabela que está sendo referenciada)
        on_delete=models.CASCADE, # Se o status for deletado, a tarefa também será deletada.
        related_name='status',    # Permite acessar as tarefas a partir de um status usando status.status.all()
        to_field='id',            # Indica que a relação usa o campo 'id' (padrão, então é opcional).
        default='1'               # Define que o status padrão é o ID 1 (pode ser problemático se esse ID não existir).
    )
   
    # Representação legível do objeto (útil no admin e no shell).
    def __str__(self):
        return self.title