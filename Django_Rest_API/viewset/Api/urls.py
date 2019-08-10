from django.urls import path,include
from rest_framework import routers
from Api import views

#register the router
router=routers.SimpleRouter()
router.register(r'heros',views.HeroViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]
