from django.db import models
from django.db.models.fields import EmailField
from django.contrib.staticfiles.templatetags.staticfiles import static
from login.models import Account
from candidate.models import Community

# Create your models here.
class Companion(models.Model):
    patron = models.DateTimeField()
    MSUser = models.ForeignKey(Account, on_delete=models.CASCADE)
    christianName = models.CharField(max_length=50, default='')
    birthDay = models.DateTimeField()
    phone = models.IntegerField(default=0)
    community = models.CharField(max_length=255, default='')
    homeLand = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    avatar = models.ImageField(null = True, blank = True)
    community_partner = models.ForeignKey(Community, on_delete= models.CASCADE)

    def __str__(self):
        return self.MSUser.fullName
    def get_image(self):
        tempt_image = self.avatar
        image = ''
        if(tempt_image):
            image = tempt_image.url
        return image
