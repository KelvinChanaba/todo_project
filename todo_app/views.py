from django.shortcuts import render
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todos': todos})
