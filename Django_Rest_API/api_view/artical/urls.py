from django.urls import path
from artical.views import ArticalView

app_name="artical"
urlpatterns = [
    path('articals/',ArticalView.as_view()),
    path('<int:pk>/',ArticalView.as_view()),
]
