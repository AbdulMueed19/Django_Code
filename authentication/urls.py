from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginf, name="login"),
    path("logout", views.logoutf, name="logout")

]