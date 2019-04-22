from django.db import models
import datetime
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
