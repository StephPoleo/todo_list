from django.urls import path
from .views import todoView, addTodoView, updateTodo
from . import views

urlpatterns = [
    path('', todoView, name='home'),
    path('addTodoItem/',addTodoView),
    path('updateTodoItem/<id>',updateTodo, name='update_todo'),
]