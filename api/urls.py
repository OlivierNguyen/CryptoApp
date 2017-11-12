from django.conf.urls import url
from api.views.bitcoin import BitcoinAPI;


urlpatterns = [
    url(r'^bitcoin/$', BitcoinAPI.as_view(), name="bitcoin"),
]