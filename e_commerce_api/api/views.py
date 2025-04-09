from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializer import UsersSerializer

@api_view(['GET'])
def get_user(request):
    users = Users.objects.all()                                                 #Get all objects from user model
    serializer = UsersSerializer(users, many=True)                              #serialize the data
    return Response(serializer.data)                                            #return data

@api_view(['POST'])
def create_user(request):
    serializer = UsersSerializer(data=request.data)                             #get data from serializer
    if serializer.is_valid():                                                   #validate the data
        serializer.save()                                                       #save the data
        return Response(serializer.data, status=status.HTTP_201_CREATED)        #return data and http response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      #return error and http response