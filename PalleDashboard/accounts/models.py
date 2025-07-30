from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# create customUser model and inherit from AbstractUser
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),  # first value will store in db and second value will display in the forms
        ('sales', "Sales")
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='sales')


class Student(models.Model):
    added_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField()
    place = models.CharField(max_length=80)
    gender = models.CharField(max_length=30)
    skillset = models.CharField(max_length=255)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name
