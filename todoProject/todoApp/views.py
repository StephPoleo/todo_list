from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import TodoModel
from .serializers import TodoSerializer

# Create your views here.
def todoView(request):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    context = {
        "object_list":queryset
    }

    return render(request, "index.html", context)

    #return render(request, 'index.html')

""" class todoView(generics.ListAPIView):
    #return render(request, 'index.html')
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
 """