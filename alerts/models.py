from django.db import models

class Alerts(models.Model):
    price = models.IntegerField(max_length=30)
    operatir = models.
    created_at = models.DateField(auto_now_add=True)
