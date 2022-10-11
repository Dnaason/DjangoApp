from django.db import models

# Create your models here.
class Detail(models.Model):
    Fname = models.CharField(max_length = 52)
    Lname = models.CharField(max_length = 52)
    Age = models.IntegerField()
    Phone = models.CharField(max_length = 43)