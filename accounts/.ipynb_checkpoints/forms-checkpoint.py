# accounts/forms.py
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    location = forms.CharField(max_length=255, required=False)

    def save(self, request):
        user = super().save(request)
        user.location = self.cleaned_data.get('location')
        user.save()
        return user
