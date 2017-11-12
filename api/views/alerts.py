from django.conf import settings
from rest_framework import generics, permissions
from rest_framework.response import Response

from alerts.models import Alerts
from ..serializers.alerts import AlertsSerializer

from coinbase.wallet.client import Client

client = Client(settings.COINBASE_API_KEY, settings.COINBASE_API_KEY)


class AlertsList(generics.ListCreateAPIView):
    model = Alerts
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AlertsSerializer

    def get_queryset(self):
        queryset = Alerts.objects.filter(created_by=self.request.user)
        return queryset


class AlertsAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alerts.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AlertsSerializer
