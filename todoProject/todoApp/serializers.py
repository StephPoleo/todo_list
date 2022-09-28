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

    is_complete = serializers.SerializerMethodField('_get_complete')

    def _get_complete(self, obj):
            if obj.is_complete == None:
                return False

            elif obj.is_complete == False:
                return False

            else:
                return True

    class Meta:

        model = TodoModel
        fields = ['id', 'name', 'is_complete', 'children', 'parent']
