from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [

    path("register/", views.signup, name="register"),
    path("login/", views.EmailLoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
]