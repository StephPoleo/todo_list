from django.shortcuts import render

from django.http import HttpResponseRedirect

from .models import TodoModel
from .serializers import TodoSerializer
from .forms import TodoForm

# Create your views here.
def todoView(request):
    submitted = False
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        queryset = TodoModel.objects.all()
        form  = TodoForm
        if 'submitted' in request.GET:
            summitted = True

    context = {
        'object_list':queryset,
        'form': form,
        'submitted': submitted
    }

    return render(request, "index.html", context)


def addTodoView(request):
    print('Nada')