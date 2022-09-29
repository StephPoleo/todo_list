from dataclasses import field
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from .serializers import TodoSerializer

from .models import TodoModel
from .forms import TodoForm, CheckedForm

# Create your views here.
def todoView(request):

    queryset = TodoModel.objects.all().order_by('id')
    data = TodoSerializer(queryset, many = True).data
    
    status_childs = []

    def count_children(data, i):

        count = len(data)-i

        """ print("Empezando con ", data[count]['name'])

        print(data[count]['parent'])
        print(len(data[count]['children'])) """

        if(len(data[count]['children'])==0 and data[count]['parent'] == None):
            """ print(data[count]['name'])
            print('Sin hijos ni papas') """
            data[count]['is_complete'] = data[count]['is_complete']
            #print(data[count]['is_complete'])

        if(len(data[count]['children'])==1):
            #print('Un hijo para ', data[count]['name'])
            if(data[count]['is_complete']):
                data[count+1]['is_complete'] = True
            #print(data[count]['children'])
            count_children(data, i-1)

        elif(len(data[count]['children'])>1):
            """ print('Varios hijos')
            print(data[count]['name']) """
            for id in data[count]['children']:

                queryset = TodoModel.objects.get(pk=id)
            
                if(queryset.is_complete == None):
                    queryset.is_complete = False

                #print(queryset)
                status_childs.append(queryset.is_complete)

            #print(status_childs)
            suma = 0
            for i in range(len(status_childs)):
                suma = suma + status_childs[i]
            #print(suma)

            if(not data[count]['is_complete']):
                if(len(status_childs) == suma):
                    #print(data[count]['name'])
                    data[count]['is_complete'] = True
                else:
                    #print(data[count]['name'])
                    data[count]['is_complete'] = False
            else:
                #print(data)
                for i in data[count]['children']:
                    #queryset = TodoModel.objects.get(pk=id)
                    TodoModel.objects.filter(pk=i).update(is_complete=True)
                    #queryset.is_complete = True
            
        
                #data = TodoSerializer(queryset, many = True).data

        # Nodo principal
        """ print('Nodo principal')
        print(data[count]['name'])
        print(data[count]['is_complete'])
        print(data[count]['parent']) """

        if(data[count]['is_complete'] and data[count]['parent']!=None):
            #print(str(data[count-1]['name']) + ' en:' + str(+data[count-1]['is_complete']))
            data[count-1]['is_complete'] = True
            #print('Cambiando a: ', data[count-1]['is_complete'])
            

  
    try:
        count_children(data, len(data))
        
    except IndexError:
        print('Lista vacia')

    print(queryset)
    print('-'*10)
    
    for i in data:
        print(i)
        print("")

    """ print("Actualizacion del queryset")
    for i in range(len(data)):
        print(data[i]['is_complete'])
        TodoModel.objects.filter(pk=data[i]['id']).update(is_complete=data[i]['is_complete'])
        #print(TodoModel.objects.filter(pk=data[i]['id']))
    
    data = TodoSerializer(queryset, many = True).data

    print(queryset)
    print('-'*10)
    print(data) """


    context = {
        'object_list':data
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
