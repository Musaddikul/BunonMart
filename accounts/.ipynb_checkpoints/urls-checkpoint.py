# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='account_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='account_reset_password'),
]
