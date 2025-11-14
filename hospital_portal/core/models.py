from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )

    role = models.CharField(max_length=20, choices=USER_TYPES, default='patient')
    profile_pic = models.ImageField(upload_to="uploads/", blank=True, null=True)

    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)

    def __str__(self):
        return self.username
