from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField()
    price=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.name
    