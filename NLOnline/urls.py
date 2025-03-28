"""
URL configuration for NLOnline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib import admin
from django.urls import path, re_path

from nlonline_antrag import views
from nlonline_antrag.views import register, new_application

urlpatterns = [
    path('', views.index),
    path('new_application/', new_application, name='new_application'),
    path('application/<int:pk>/', views.AntragDetailView.as_view(), name='application-detail'),
    path('application/', views.AntragListView.as_view(), name='application-list'),
    re_path('media/(?P<path>.*)', views.mediaView, name='media'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register')
]
