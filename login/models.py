from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    status = models.BooleanField(default=True)
    choice_option =((0,"Candidate"),(1,"Partner"), (2,"Teacher"))
    option = models.IntegerField(choices=choice_option, default=0)
    MSUser = models.IntegerField(default=0)
    fullName = models.CharField(default='', max_length=255)

    def get_name(self):
        return self.first_name
