from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name = 'home'),
    path('login/', views.loginview, name = 'login'),
    path('signup/', views.signupview, name = 'signup'),
    path('history/', views.historyview, name = 'history'),
    path('logout/', views.logoutview, name = 'logout'),
]