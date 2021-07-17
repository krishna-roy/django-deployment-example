"""ProTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from polls import views

app_name='voter_list'

urlpatterns = [
    path("user_register/",views.user_register,name='user_register'),
    
    path('users/', views.get_users,name='get_users'),

    path('help/',views.help,name='contact_us'),

    path('registeremployee/',views.register_employee,name='register_employee'),
    path('login_me/',views.login_employee,name='login_employee'),

    path('logout_me/',views.employee_logout,name='employee_logout')
]
