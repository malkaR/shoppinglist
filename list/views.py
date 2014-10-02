from rest_framework import viewsets
from django.contrib.auth.models import User
from models import ListItem
from serializers import UserSerializer, ListItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer