from django.urls import path, include
from . import views
from .views import *
from rest_framework_nested import routers


urlpatterns = [
    path('leads/', LeadList.as_view()),
    path('leads/image/<path:image>', ImageServeView.as_view(), name='image_serve')
]