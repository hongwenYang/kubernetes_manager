from django.urls import path
from .views import *

urlpatterns = [
    path('list_pods/', list_pods, name='list_pods'),
]