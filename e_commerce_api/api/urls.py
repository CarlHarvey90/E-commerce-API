from django.urls import path
from .views import get_users, create_user, user_detail, index, login_view, signup, welcome

urlpatterns = [
    #path('users/', views.users, name ='users'),
    path("", index, name="index"),
    path("login_view/", login_view, name="login_view"),
    #path("login_request/", login_request, name="login_request"),
    path("signup/", signup, name="signup"),
    path("get_users/", get_users, name="get_users"),
    path("create_user/", create_user, name="create_user"),
    path("user/<int:pk>", user_detail, name="user_detail"),
    path("welcome/", welcome, name="welcome"),
]