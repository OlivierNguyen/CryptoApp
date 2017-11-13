from __future__ import absolute_import, unicode_literals
from alerts.celery import app


@app.task(name='periodically_check_bitcoin_price')
def periodically_check_bitcoin_price():
    print("hoho :)")
    return "hello"
