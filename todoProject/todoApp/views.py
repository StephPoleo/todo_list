from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from .models import TodoModel
from .forms import TodoForm

# Create your views here.
def todoView(request):
    queryset = TodoModel.objects.all()
    context = {
        'object_list':queryset
    }

    return render(request, "todo_list.html", context)


def addTodoView(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, "new_todo.html", context)

def updateTodo(request, id):
    queryset = TodoModel.objects.get(pk=id)
    form = TodoForm(request.POST or None, instance=queryset)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'todo':queryset,
        'form':form
    }
    return render(request, "update_todo.html", context)