from django.contrib import admin
from django.urls import path
from .views import *
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

urlpatterns = [
    path('', IndexView, name='index')
]
