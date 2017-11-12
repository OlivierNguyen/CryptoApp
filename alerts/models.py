from django.db import models
from .enums.operator import OPERATOR


class Alerts(models.Model):
    price = models.IntegerField(max_length=30)
    operator = models.CharField(choices=OPERATOR, max_length=3)
    sent_at = models.DateField()
    created_at = models.DateField(auto_now_add=True)
