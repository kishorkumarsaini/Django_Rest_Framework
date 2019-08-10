from django.urls import path
from song.views import SongAPIView


app_name="song"

urlpatterns = [
    path('song/',SongAPIView.as_view()),
    path('song/<int:pk>',SongAPIView.as_view()),
]
