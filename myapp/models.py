from django.db import models
from django.utils import timezone

class temperature_db(models.Model):
    sensor_id = models.IntegerField(null=False)
    temperature = models.FloatField(null=False)
    humidity = models.FloatField(null=False)
    datetime = models.DateTimeField(null=False)

class temperature_db2(models.Model):
    sensor_id = models.IntegerField(default=40) #若無資料，則預設40
    temperature = models.FloatField(null=False)
    humidity = models.FloatField(null=False)
    datetime =  models.DateTimeField(auto_now=True) #自動填入日期
