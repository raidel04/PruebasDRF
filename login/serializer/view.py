from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
 

@api_view(['GET','POST','PUT','DELETE'])
def hello_world(request):

    if request.method == 'POST':
        return HttpResponse("haz creado algo nuevo")

    if request.method == 'PUT':
        return HttpResponse("Lo acabas de modificar")

    if request.method == 'DELETE':
        return Response({'message':'eleminado'})

    if request.method == 'GET':
        return Response({'message': 'Que haces ahora'})

    return Response({'message':'Hola'})