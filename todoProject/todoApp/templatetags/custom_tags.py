# create the register instance by initializing it with the Library instance.
from django import template
from ..models import TodoModel
from ..serializers import TodoSerializer

register = template.Library()

@register.filter(name='upper')
def upper(value):
  query = TodoModel.objects.all()
  num = []
  for q in query:
    num.append(str(q).split(' -')[0])


@register.inclusion_tag('prueba.html')
def recursive(value):

  query = TodoModel.objects.filter(pk__in=value)
  data = TodoSerializer(query, many = True).data

  """ lista = []
  print("VALOR: ", value)
  for id in value:
    query = TodoModel.objects.get(pk=id)
    lista.append(query)
    print(query)

  data = TodoSerializer(lista, many = True).data
  print("Data2: ", data) """

  return {'users': data}