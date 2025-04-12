from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializer import UsersSerializer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth

@api_view(['GET'])
def get_users(request):
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

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = UsersSerializer(user, data=request.data)                             
        if serializer.is_valid():                                                   
            serializer.save() 
            return Response(serializer.data)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

#def login_view(request):
#    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("welcome")
        else:
             # Login failed — show error
            return render(request, 'login.html', {
                'error': 'Invalid username or password.'
            })  
    else:
        #form = AuthenticationForm()
        return render(request, 'login.html') 

def signup(request):
    return render(request, 'signup.html')

def welcome(request):
    return render(request, 'welcome.html')
