from rest_framework import serializers
from artical.models import Artical

class ArticalSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=200)
    description=serializers.CharField()
    body=serializers.CharField()
    author_id=serializers.IntegerField()

    def create(self,validated_data):
        return Artical.objects.create(**validated_data)


    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        instance.body=validated_data.get('body',instance.body)
        instance.author_id=validated_data.get('author_id',instance.author_id)
        instance.save()
        return instance
    