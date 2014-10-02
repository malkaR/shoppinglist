from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from models import ListItem, List, User
from serializers import UserSerializer, ListItemSerializer, ListSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

    @detail_route(methods=['DELETE'])
    def delete(self, request, pk=None):
        self.get_object().delete()
        return Response({'deleted':'true'})


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = 'slug'

    def pre_save(self, obj):
        user = User.objects.get(is_admin=False)
        setattr(obj, 'user_id', user.id)
