from django.contrib import admin
from myapp.models import Status, TodoList

# Register your models here.
admin.site.register(Status)
admin.site.register(TodoList)
