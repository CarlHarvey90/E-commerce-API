from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import generics
from .models import Users
from.serializers import UsersSerializer

class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

def users(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())