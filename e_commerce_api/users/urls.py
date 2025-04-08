from django.urls import path
from . import views

urlpatterns = [
    #path('users/', views.users, name ='users'),
    path("users/", views.UsersListCreate.as_view(), name="users-view-create")
]