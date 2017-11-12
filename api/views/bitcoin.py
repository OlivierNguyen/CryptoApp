from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class BitcoinAPI(APIView):
    queryset = User.objects.all()

    def get(self, request):
        return Response("hello")
