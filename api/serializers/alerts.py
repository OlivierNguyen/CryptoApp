from rest_framework import serializers

from alerts.models import Alerts


class AlertsSerializer(serializers.ModelSerializer):

    class Meta:
            model = Alerts
            fields = (
                'id',
                'price',
                'operator',
                'created_at',
                'created_by',
            )
