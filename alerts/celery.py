from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptoapp.settings')

app = Celery('cryptoapps')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.on_after_configure.connect
def setup_periodic_tasks(**kwargs):
    app.add_periodic_task(10.0, periodically_check_bitcoin_price.s(), name='check BTC every 10sec')

# FIXME https://stackoverflow.com/questions/41119053/connect-new-celery-periodic-task-in-django/46965132#46965132
@app.task
def periodically_check_bitcoin_price():
    from .tasks import periodically_check_bitcoin_price
    periodically_check_bitcoin_price()
