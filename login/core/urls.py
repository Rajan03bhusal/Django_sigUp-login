from django.urls import path
from django.contrib import admin
from .import views
from .views import *
urlpatterns = [
    path('', views.Home,name="home"),
    path('Sigup', SingupView.as_view(),name="Sigup"),
    path('Login', MyloginView.as_view(),name="Login")


]