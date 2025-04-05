from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import serializer
 
class MyAppi(APIView):
    def get(self,request,pk= None):
        return Response({'message':'hola como estas'})
    
    def post(self,request,pk = None):
        return HttpResponse("creado")
    
    def put(self,request,pk= None):
        return HttpResponse('modificado')
    
    def delete(self,request,pk = None):
        return HttpResponse('delete')

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer

class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer
