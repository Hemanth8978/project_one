from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(User):
    phone=models.IntegerField()
    gender=models.CharField(max_length=10,choices=[['male','male'],['female','female']])
    date_of_birth=models.DateField()
    otp=models.IntegerField(null=True,blank=True)
    otp_expiry=models.DateTimeField(null=True,blank=True)