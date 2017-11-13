from __future__ import absolute_import, unicode_literals
import operator
from decimal import Decimal
from django.conf import settings
from alerts.celery import app
from coinbase.wallet.client import Client

from alerts.models import Alerts
from alerts.enums.operator import OPERATOR, EQ, GT, GTE, LT, LTE
from .utils import send_alert_email

client = Client(settings.COINBASE_API_KEY, settings.COINBASE_API_KEY)

@app.task(name='periodically_check_bitcoin_price')
def periodically_check_bitcoin_price():
    data_btc = client.get_buy_price(currency_pair='BTC-USD')
    price_btc = Decimal(data_btc['amount'])

    # Get alerts which are not sent yet
    alerts = Alerts.objects.filter(sent_at__isnull=True).only('price', 'operator', 'created_by',)

    for alert in alerts:
        alert_price = Decimal(alert.price)
        alert_operator = alert.operator

        compare_function = {
            EQ: operator.eq,
            GT: operator.gt,
            GTE: operator.ge,
            LT: operator.lt,
            LTE: operator.le,
        }

        should_alert = compare_function[alert_operator](price_btc, alert_price)

        if should_alert:
            message = ('{} is {} than {}').format(price_btc, dict(OPERATOR)[alert_operator], alert_price)
            print(message) # For debug
            send_alert_email(message, alert.created_by.email)
