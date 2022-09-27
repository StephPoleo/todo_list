from django import forms
from django.forms import ModelForm
from .models import TodoModel

from rest_framework import serializers

class TodoForm(ModelForm):

    class Meta:
        model = TodoModel
        fields = ['id', 'name', 'is_complete', 'parent']