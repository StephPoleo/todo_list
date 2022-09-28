from django.urls import path
from .views import todoView, addTodoView, updateField, updateTodo, deleteTodo
from . import views

urlpatterns = [
    path('', todoView, name='home'),
    path('addTodoItem/',addTodoView),
    path('updateTodoItem/<int:id>',updateTodo, name='update_todo'),
    path('<int:id>',updateField, name='update_field'),
    path('deleteTodoItem/<int:id>',deleteTodo, name='delete_todo'),
]