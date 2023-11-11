from django.db import models

# Create your models here.
class signuptbl(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

class product(models.Model):
    name=models.CharField(max_length=255)
    quantity=models.IntegerField()
    price=models.IntegerField()
    amount=models.IntegerField(null=True)
