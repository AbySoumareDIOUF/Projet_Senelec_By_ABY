from django import views
from django.urls import path,include
from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name='login'),

]
