from django.urls import path
from .views import ask_mbweubot

urlpatterns = [
    path("ask/", ask_mbweubot),
]
