from django.shortcuts import render,get_object_or_404
from song.models import Song
from rest_framework.response import Response
from rest_framework.views import APIView
from song.serializers import SongSerializer

# Create your views here.

class SongAPIView(APIView):

    def get(self,request,*args,**kwargs):
        songs=Song.objects.all()
        serializer=SongSerializer(songs,many=True)
        return Response({"songs":serializer.data})

    def post(self,request):
        song=request.data.get('song')
        serializer=SongSerializer(data=song)
        if serializer.is_valid(raise_exception=True):
            song_saved=serializer.save()
        return Response({"Success":" Song '{}' is successfully created".format(song_saved.title)})

    def put(self,request,pk):
        saved_data=get_object_or_404(Song.objects.all(),pk=pk)
        data=request.data.get('song')
        serializer=SongSerializer(instance=saved_data,data=data,partial=True)
        
        if serializer.is_valid(raise_exception=True):
            song_saved=serializer.save()
        return Response({"Success":"Song  '{}' successfully updated".format(song_saved.title)})
        
    def delete(self,request,pk):
        song=get_object_or_404(Song.objects.all(),pk=pk)
        song.delete()
        return Response({"Success":"Song id  '{}' successfully deleted".format(pk)},status=204)