from django.db import models
from django.conf import settings
from shop.models import Category

class CustomOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='custom_designs/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    notes = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Custom Order by {self.user.email}"
