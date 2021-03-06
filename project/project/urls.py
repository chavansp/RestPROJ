"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from app1.views import UserLoginView,logoutView
# from rest_framework import routers
#
# rout = routers.DefaultRouter()
# rout.register('user',Userview,basename='User')
# from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns=[
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logoutView.as_view(), name='auth_logout'),
]
