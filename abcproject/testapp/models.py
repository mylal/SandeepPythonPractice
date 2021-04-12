from django.db import models

# Create your models here.
class Employee(models.Model):
    id1=models.IntegerField()
    name=models.CharField(max_length=30)
    dept=models.CharField(max_length=30)