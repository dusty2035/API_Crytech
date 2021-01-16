from django.urls import path , include
from rest_framework.authtoken import views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('' , views.EventViewSet)

urlpatterns = [
    path('' , include(router.urls))
]
