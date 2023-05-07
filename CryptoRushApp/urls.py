from django.urls import path,include
from .views import About,Index,Track,signup,logout,login,feature,Error
from . import views
from django.contrib import admin
from django_otp.admin import OTPAdminSite

admin.site.__class__ = OTPAdminSite




urlpatterns = [
    path('',views.Index,name="home"),
    path('about/',views.About,name="about"),
    path('Track/',views.Track,name="track"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.Logout,name="logout"),
    path('login/', views.Login, name='login'),
    path('feature/', views.feature, name='feature'),
    path('404/', views.Error, name='404'),
    path('user/<int:pk>/profile/',views.Profile,name="profile"),
    path('exchange/',views.exchange,name="exchange"),
    path('crypto/',views.crypto,name="crypto"),
    path('aboutcrypto/',views.aboutcrypto,name="aboutcrypto"),
]
