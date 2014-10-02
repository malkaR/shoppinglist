from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListItem
        fields = ('item', 'quantity', 'store', 'date_added')

