from django.urls import path
from .views import *

urlpatterns = [
    path('', todoView),
    path('addTodoItem/',addTodoView), 
]