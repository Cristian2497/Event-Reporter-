from djongo import models
from pymongo import mongo_client

# Create your models here.


class EventReported(models.Model):
    time = models.JSONField
    location = models.JSONField
    alert_code = models.JSONField
    describtion = models.JSONField
    image = models.JSONField
    tag = models.JSONField

