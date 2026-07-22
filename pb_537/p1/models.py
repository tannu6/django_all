from django.db import models

# Create your models here.
class Event(models.Model):
    name=models.CharField()
    date=models.DateField()
    location=models.CharField()
    def __str__(self):
        return self.name