from django.shortcuts import render, redirect
#from django.template import loader
#from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
#from .models import Users
from Products.models import Products
from .serializer import UsersSerializer
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
#from django import forms
from .forms import SignUpForm
from Cart.views import view_cart

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()                                                  #Get all objects from user model
        serializer = UsersSerializer(users, many=True)                              #serialize the data
        return Response(serializer.data)                                            #return data
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)                                           

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def auth_test(request):
    return Response({'authenticated_user': request.user.username})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    serializer = UsersSerializer(data=request.data)                             #get data from serializer
    if serializer.is_valid():                                                   #validate the data
        serializer.save()                                                       #save the data
        return Response(serializer.data, status=status.HTTP_201_CREATED)        #return data and http response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      #return error and http response

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
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

#def index(request):
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render())
    
def index(request):
    return render(request, 'index.html')

# def products(request):
#     products = Products.objects.all() #get_all_products()
#     print("products")
#     print(products)
#     return render(request, 'products.html', {'products': products})

# def cart(request):
#     view_cart(request)
#     return render(request, 'cart.html')


#def login_view(request):
#    return render(request, 'login.html')

def logged_out(request):
    logout(request)
    return render(request, 'logged_out.html')

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
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect("welcome")
        else:
             # Signup failed — show error
            return render(request, 'signup.html', {
                'error': 'Something went wrong, please try again.'
            }) 
    return render(request, 'signup.html', {'form':form} )

def welcome(request):
    return render(request, 'welcome.html')
