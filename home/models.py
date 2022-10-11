from email.headerregistry import Address
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User(models.Model):
    Fname = models.CharField(max_length=45)
    Lname = models.CharField(max_length=45)
    Address = models.CharField(max_length=45)
    Age = models.CharField(max_length=100)

class Clients(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    repassword = models.CharField(max_length=50)