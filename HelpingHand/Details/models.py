from django.db import models

# Create your models here.
class Details(models.Model):
    image = models.ImageField(upload_to='media/',default="")
    address = models.CharField (max_length = 200)
    description = models.CharField(max_length = 5000)
