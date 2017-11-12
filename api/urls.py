from django.conf.urls import url
from api.views.bitcoin import BitcoinAPI
from api.views.alerts import AlertsList, AlertsAPI

urlpatterns = [
    url(r'^bitcoin/$', BitcoinAPI.as_view(), name="bitcoin"),
    url(r'^alerts/$', AlertsList.as_view(), name="alerts-list"),
    url(r'^alerts/(?P<pk>[0-9]+)/$', AlertsAPI.as_view(), name="alerts-api"),
]