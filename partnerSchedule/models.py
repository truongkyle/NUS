from django.db import models
from partner.models import Companion
from candidate.models import Candidate
import datetime
# Create your models here.
class PartnerSchedule(models.Model):
    x = datetime.datetime.date()
    IDPartner = models.ForeignKey(Companion, on_delete= models.CASCADE)
    IDCandidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    IDDate = models.IntegerField(default=0)#0101
    CreatedDate = models.DateField(default=x)