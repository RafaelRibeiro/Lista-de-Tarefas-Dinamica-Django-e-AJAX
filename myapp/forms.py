from django import forms     # Importa o módulo de formulários do Django.
from .models import TodoList # Importa o modelo TodoList que será utilizado no formulário.

# Define um formulário baseado no modelo TodoList.
class TodoListForm(forms.ModelForm):

    # Informações de configuração do formulário.
    class Meta:
        model = TodoList      # Indica que o formulário se baseia no modelo TodoList.
        fields = ('title',)   # Campos que serão exibidos no formulário.
        exclude = ('status',) # Remove o campo 'status' do formulário.

    # Método especial chamado na criação do formulário.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Inicializa o formulário herdando o comportamento padrão do ModelForm.

        # Adiciona a classe CSS 'form-control' do Bootstrap a todos os campos do formulário, para melhorar o estilo visual no frontend.
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'