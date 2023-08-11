import random
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

def generate_confirmation_code():
    return ''.join(random.choices('0123456789', k=6))