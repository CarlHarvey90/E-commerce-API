from rest_framework import serializers
from django.contrib.auth.models import User
#from .models import Users

# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ["id", "firstname", "lastname", "email", "username", "password"]


#https://docs.djangoproject.com/en/5.2/ref/contrib/auth/
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password"]
