from django.db import models
from django.utils import timezone

# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date1 = models.DateField(default=timezone.now)




    def __str__(self):
        return self.name
