from django.urls import path
from login.serializer import view

urlpatterns = [
    path("", view.hello_world, name = ""),
    ]