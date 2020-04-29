"""bloodbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from bloodbankapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login,name='login'),
    path('logout',Logout,name='logout'),
    path('search',search,name='search'),
    path('home',indexpage,name='home'),
    path('login',Login,name='login'),
    path('addhospital',Addhospital,name='addhospital'),
    path('viewhospital',viewhospital,name="viewhospital"),
    path('reg',reg,name='reg'),
    path('bloodreq',bloodreq,name='bloodreq'),
    path('viewreq',viewreq,name="viewreq"),
    path('donateblood',donateblood,name='donateblood'),
    path('^edit_delete_hospital/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',Edit_Delete_hospital,name="edit_delete_hospital"),
    path('^message/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',message,name="message"),
]
