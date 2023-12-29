from .views import *
from django.urls import path
from django.contrib.auth import views as django_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', django_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', django_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile')
]