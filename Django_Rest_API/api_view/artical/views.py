from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from artical.models import Author,Artical
from artical.serializers import ArticalSerializer
# Create your views here.


class ArticalView(APIView):
    def get(self,request,*args, **kwargs):
        articals=Artical.objects.all()
        serializer=ArticalSerializer(articals,many=True)
        return Response({"articals": serializer.data})
    
    def post(self,request):
        artical = request.data.get('artical')
        #create a artical from above data
        serializer=ArticalSerializer(data=artical)

        if serializer.is_valid(raise_exception=True):
            article_saved=serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
        
    def put(self,request,pk):
        saved_data=get_object_or_404(Artical.objects.all(),pk=pk)
        data=request.data.get('artical')
        serializer=ArticalSerializer(instance=saved_data,data=data,partial=True)
        
        if serializer.is_valid(raise_exception=True):
            article_saved=serializer.save()
        return Response({"Success":"Article '{}' updated successfully".format(article_saved.title)})

    
    def delete(self,request,pk):
        #get the article with this pk
        article=get_object_or_404(Artical.objects.all(),pk=pk)
        article.delete()
        return Response({"message": "Artical with '{}' id deleted successfully".format(pk)},status=204)