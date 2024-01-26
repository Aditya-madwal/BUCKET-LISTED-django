from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name = 'home'),
    path('login/', views.loginview, name = 'login'),
    path('signup/', views.signupview, name = 'signup'),
    path('<str:user>/history/', views.historyview, name = 'history'),
    path('logout/', views.logoutview, name = 'logout'),
    path('<str:user>/ordered/<str:itemid>', views.orderedview, name = 'ordered'),
    path('<str:user>/delete/<str:itemid>', views.deleteview, name = 'delete'),
]
