from __future__ import absolute_import, unicode_literals
from alerts.celery import app

# FIXME https://stackoverflow.com/questions/41119053/connect-new-celery-periodic-task-in-django/46965132#46965132
@app.task(name='periodically_check_bitcoin_price')
def periodically_check_bitcoin_price():
    print("hoho :)")
    return "hello"
