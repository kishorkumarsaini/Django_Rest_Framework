from rest_framework import serializers
from demo_project.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=('id','title','description')