from django.shortcuts import render
from demo_project.serializer import  TodoSerializer
from rest_framework import generics
from demo_project.models import Todo

# Create your views here.

class TodoListView(generics.ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer



class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    