from django.urls import path
from .views import get_users, create_user, user_detail, index, login, signup

urlpatterns = [
    #path('users/', views.users, name ='users'),
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("get_users/", get_users, name="get_users"),
    path("create_user/", create_user, name="create_user"),
    path("user/<int:pk>", user_detail, name="user_detail")
]