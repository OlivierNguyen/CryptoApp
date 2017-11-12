from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

from coinbase.wallet.client import Client

client = Client(settings.COINBASE_API_KEY, settings.COINBASE_API_KEY)


class BitcoinAPI(APIView):
    queryset = User.objects.all()

    def get(self, request):
        price_btc_usd = client.get_buy_price(currency_pair='BTC-USD')
        return Response(price_btc_usd)
