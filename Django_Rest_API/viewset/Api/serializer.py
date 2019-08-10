from rest_framework import serializers
from Api.models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Hero
        fields=('name','alias')