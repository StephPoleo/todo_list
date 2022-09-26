from rest_framework import serializers

from .models import TodoModel

class TodoSerializer(serializers.ModelSerializer):
    children = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=TodoModel.objects.all(),
        required=False
    )
    parent = serializers.PrimaryKeyRelatedField(
        queryset=TodoModel.objects.all(),
        required=False
    )

    class Meta:
        model = TodoModel
        fields = ['id', 'name', 'is_complete', 'children', 'parent']