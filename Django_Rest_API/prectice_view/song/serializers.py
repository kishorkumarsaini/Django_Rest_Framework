from rest_framework import serializers
from song.models import Song

class SongSerializer(serializers.ModelSerializer):
    
    title=serializers.CharField(max_length=120)
    description=serializers.CharField()
    singer_id=serializers.IntegerField()
    '''
    class Meta :
        model=Song
        fields=['singer_id','title','description']
    '''
    def create(self,validated_data):
        return Song.objects.create(**validated_data)
    

    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        instance.singer_id=validated_data.get('singer_id',instance.singer_id)
        instance.save()
        return instance