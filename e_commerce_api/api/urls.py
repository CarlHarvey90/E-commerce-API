from django.urls import path
from .views import get_user, create_user

urlpatterns = [
    #path('users/', views.users, name ='users'),
    path("get_user/", get_user, name="get_user"),
    path("create_user/", create_user, name="create_user")
]