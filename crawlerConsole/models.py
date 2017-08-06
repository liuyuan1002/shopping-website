from django.db import models

# Create your models here.

class pcList(models.Model):
    processName = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    host = models.CharField(max_length=20,default='127.0.0.1')
    path = models.CharField(max_length=255,default='/')

    def __str__(self):
        return self.name
