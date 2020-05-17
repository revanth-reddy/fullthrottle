from django.db import models
from django.utils import timezone
import datetime
import time

# Create your models here.
class member(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=20)

    def __unicode__(self):
        return self.real_name


class activity(models.Model):
    # start_time = models.DateTimeField(default=datetime.datetime.now)
    # end_time = models.DateTimeField(default=datetime.datetime.now)
    start_time = models.CharField(max_length=30)
    end_time = models.CharField(max_length=30)
    member = models.ForeignKey(member, related_name='activity_periods', on_delete=models.CASCADE)

    # def __unicode__(self):
    #     return self.start_time

    # def __str__(self):
    #     return '{start_time: %s},{end_time: %s}' % (self.start_time, self.end_time)