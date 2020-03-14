from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Questions(models.Model):
    ques = models.TextField()
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.ques

    def publish_date(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    ques = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text
