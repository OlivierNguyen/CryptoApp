from __future__ import absolute_import, unicode_literals
from celery import shared_task
from alerts.celery import app


@app.on_after_configure.connect
def setup_periodic_tasks(**kwargs):
    app.add_periodic_task(5.0, periodically_check_bitcoin_price.s(), name='check BTC every 10sec')


# FIXME https://stackoverflow.com/questions/41119053/connect-new-celery-periodic-task-in-django/46965132#46965132
@app.task(name='periodically_check_bitcoin_price')
def periodically_check_bitcoin_price():
    print("hoho")
    return "hello"
