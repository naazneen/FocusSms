from django.db import models

# Create your models here.

from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User


# Create your models here.

class Patient(models.Model):
    # manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    gender = models.CharField(max_length=20, choices=(('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')))
    date_of_birth = models.DateTimeField(default=datetime.now())
    phone_number = models.CharField(max_length=13)
    added_by=models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.firstname


