import datetime

from django.db import models

# Create your models here.
class Task(models.Model):
    goal = models.CharField(max_length=100)
    time_created = models.DateField(default=datetime.datetime.now)

    # equivalent of toString
    def __str__(self):
        return "Goal: "+self.goal