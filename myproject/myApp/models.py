from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class registration(models.Model):
    rgID = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    father_name = models.CharField(max_length=225)
    college = models.CharField(max_length=225)
    contact_no=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    time_period = models.CharField(max_length=225)

class TrainerSignIn(models.Model):
    empID = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
