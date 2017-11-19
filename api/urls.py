from django.conf.urls import url
from api.views.bitcoin import BitcoinAPI
from api.views.alerts import AlertsList, AlertsAPI
from api.views.users import UserList, UserAPI
from api.views.login import Login

urlpatterns = [
    url(r'^bitcoin/$', BitcoinAPI.as_view(), name="bitcoin"),
    url(r'^alerts/$', AlertsList.as_view(), name="alerts-list"),
    url(r'^alerts/(?P<pk>[0-9]+)/$', AlertsAPI.as_view(), name="alerts-api"),
    url(r'^users/$', UserList.as_view(), name="users-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', UserAPI.as_view(), name="users-api"),
    url(r'^login/$', Login.as_view(), name="login"),
]
