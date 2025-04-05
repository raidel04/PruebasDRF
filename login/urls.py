from django.urls import path
from . import view
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("", view.MyAppi.as_view(), name="lista"),  # Sin PK (GET, POST)
    path("<int:pk>/", view.MyAppi.as_view(), name="detalle"),  # Con PK (GET, PUT, DELETE)
    path('user/',view.UserListCreateView.as_view(),name='all_users'),
    path('user/<int:pk>',view.UserView.as_view(),name = 'single_user')
]