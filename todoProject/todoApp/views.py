from dataclasses import field
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from .serializers import TodoSerializer

from .models import TodoModel
from .forms import TodoForm, CheckedForm

# Create your views here.
def todoView(request):
    queryset = TodoModel.objects.all()

    data = TodoSerializer(queryset, many = True).data

    status_childs = []
    
    # Calculate the status of a branch
    for i in range(len(data)):
        # If the branch has children, is the only way it can change
        if(data[i]['children']):
            for id in data[i]['children']:
                # We search for the children with their ids, too see if their tasks are complete
                queryset = TodoModel.objects.get(pk=id)
                if(queryset.is_complete == None):
                    queryset.is_complete = False

                status_childs.append(queryset.is_complete)
            
            # If the children tasks are complete and everything is true, set the parent is_complete to True
            if(len(status_childs) == (status_childs[0]+status_childs[1])):
                data[i]['is_complete'] = True
            else:
                data[i]['is_complete'] = False

    context = {
        'object_list':data,
        'query': queryset
    }

    return render(request, "index.html", context)


def addTodoView(request):
    form = TodoForm
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

def updateField(request, id):
    queryset = TodoModel.objects.get(pk=id)

    if(queryset.is_complete):
        queryset.is_complete=False
    elif(not queryset.is_complete):
        queryset.is_complete=True

    form = CheckedForm(request.POST or None, instance=queryset)
    
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'todo':queryset,
        'form':form
    }
    return render(request, "update_field.html", context)

def deleteTodo(request, id):
    queryset = TodoModel.objects.get(pk=id)
    queryset.delete()
    return redirect('home')
