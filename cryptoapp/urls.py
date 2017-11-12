from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # Login and logout views for the browsable API
]
