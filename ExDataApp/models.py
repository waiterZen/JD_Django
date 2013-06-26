from django.db import models

# Create your models here.


class Product(models.Model):
     name          = models.CharField(max_length = 100)
     errorDate     = models.CharField(max_length = 100)
     errorType     = models.CharField(max_length = 600)
     specialGas     = models.TextField(max_length = 600)
     threeRatio     = models.TextField(max_length = 600)
     useMethod      = models.TextField(max_length = 600)
     advantage      = models.TextField(max_length = 2000,null=True)


