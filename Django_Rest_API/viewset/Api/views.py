from django.shortcuts import render
from rest_framework import viewsets
from Api.serializer import HeroSerializer
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet):
    queryset=Hero.objects.all()
    serializer_class=HeroSerializer