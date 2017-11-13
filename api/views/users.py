from django.conf import settings
from rest_framework import generics, permissions
from django.contrib.auth.models import User

from ..serializers.users import UserSerializer

class UserList(generics.ListCreateAPIView):
    model = User
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
