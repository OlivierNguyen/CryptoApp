from django.db import models
from django.conf import settings

from .enums.operator import OPERATOR, EQ


class Alerts(models.Model):
    price = models.IntegerField(max_length=30)
    operator = models.CharField(choices=OPERATOR, max_length=3, default=EQ)
    sent_at = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(auto_now_add=True)
