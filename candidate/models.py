from django.db import models
from django.db.models.fields import IntegerField
from login.models import Account
from django.contrib.staticfiles.templatetags.staticfiles import static
import datetime



# Create your models here.
class Community(models.Model):
    x = datetime.datetime.now()
    patron = models.DateTimeField(null= True, blank= True, default=x)
    christian = models.CharField(max_length=50, default='')
    communityName = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.communityName

class Candidate(models.Model):
    x = datetime.datetime.now()
    b =datetime.date.today()
    MSUser = models.ForeignKey(Account, on_delete=models.CASCADE)
    christianName = models.CharField(max_length=50, default='')
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    patron = models.DateTimeField(null= True, blank= True, default=x)
    birthDay = models.DateField(blank= True, default=b)
    phone = models.IntegerField(default=0, null= True)
    homeLand = models.CharField(max_length=50, blank= True)
    status = models.BooleanField(default=True)
    avatar = models.ImageField(null = True, blank = True)

    def get_image(self):
        tempt_image = self.avatar
        image = static('') #default image_path for avatar
        if (tempt_image):
            image = tempt_image.url
        return image
    def __str__(self):
        return self.MSUser.fullName


    

