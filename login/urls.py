from django.urls import path
from login.serializer.view import MyAppi
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("", MyAppi.as_view(), name="lista"),  # Sin PK (GET, POST)
    path("<int:pk>/", MyAppi.as_view(), name="detalle"),  # Con PK (GET, PUT, DELETE)
]