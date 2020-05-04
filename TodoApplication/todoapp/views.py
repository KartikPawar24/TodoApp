from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItemList


def todoappView(request):
    all_todo_items = TodoItemList.objects.all()
    return render(request, 'todolist.html',
                  {'all_items': all_todo_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = TodoItemList(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, i):
    y = TodoItemList.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')
