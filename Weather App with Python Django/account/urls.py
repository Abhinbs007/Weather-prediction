from django.urls import path
from .import views
from django.contrib import admin
from account import views

urlpatterns  =[
      path('', views.index, name='index'),

    path('register',views.register ,name='register'),
     path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
     path('about',views.about,name='about'),
     path('', views.home_view, name='home'), 
     
    path('feedback/', views.feedback_view, name='feedback'),


]