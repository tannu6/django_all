from django.db import models

# Create your models here.
class Event(models.Model):
    name=models.CharField()
    organizer=models.CharField()
    venue=models.CharField()
    event_date=models.DateField()
    event_time=models.TimeField()
    ticket=models.IntegerField()
    capacity=models.IntegerField()
    description=models.CharField()
    def __str__(self):
        return self.name