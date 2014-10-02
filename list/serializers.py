from django.contrib.auth.models import User
from models import ListItem, List
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListItem
        fields = ('item', 'quantity', 'store', 'date_added')

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('user__name', 'name', 'list_item_count', 'date_modified')


