from django.db import models

class UserData(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 30)

