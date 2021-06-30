from django.db import models
from login.models import Account
import datetime
# Create your models here.
class Teacher(models.Model):
    MSUser = models.ForeignKey(Account, on_delete=models.CASCADE)
    x = datetime.datetime.now()
    christianName = models.CharField(max_length=50, default='', null= True, blank= True)
    birthDay = models.DateField(null= True, blank= True)
    phone = models.IntegerField(default=0)
    homeLand = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    avatar = models.ImageField(null = True, blank = True)