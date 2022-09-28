# create the register instance by initializing it with the Library instance.
from django import template
from ..models import TodoModel
from ..serializers import TodoSerializer

register = template.Library()

@register.filter(name='upper')
def upper(value):
  print(value)
  query = TodoModel.objects.all()
  num = []
  for q in query:
    num.append(str(q).split(' -')[0])


@register.inclusion_tag('prueba.html')
def recursive(value):
    query = TodoModel.objects.filter(pk__in=value)
    data = TodoSerializer(query, many = True).data
    print(data)
    return {'users': data}