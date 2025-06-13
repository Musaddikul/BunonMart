from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.utils.translation import gettext_lazy as _

# class RegisterView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     template_name = "registration/register.html"
#     success_url = reverse_lazy("account_login")
