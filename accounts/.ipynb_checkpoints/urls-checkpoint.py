from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'), name='reset_password'),
    # Add password reset confirm, complete, etc.
]
