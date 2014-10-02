from models import ListItem, List, User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    is_admin = serializers.Field(source='is_admin')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_admin')

class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='listitem-detail',
        lookup_field='pk'
    )

    list = serializers.HyperlinkedRelatedField(
        view_name='list-detail',
        lookup_field='slug'
    )

    class Meta:
        model = ListItem
        fields = ('item', 'quantity', 'store', 'date_added', 'date_modified', 'list', 'url')

class ListSerializer(serializers.HyperlinkedModelSerializer):
    item_count = serializers.Field(source='list_item_count')
    items = serializers.RelatedField(many=True, source='listitem_set.all')
    user = serializers.Field(source='user')
    url = serializers.HyperlinkedIdentityField(
        view_name='list-detail',
        lookup_field='slug'
    )

    class Meta:
        model = List
        fields = ('name', 'date_modified', 'user', 'item_count', 'items', 'url')
