from django.conf.urls import patterns, include, url
from rest_framework import routers
from list.views import UserViewSet, ListItemViewSet, ListViewSet
from list import routers as list_routers

router = routers.DefaultRouter()
router.register(r'items', ListItemViewSet)
router.register(r'lists', ListViewSet)

router_readonly = list_routers.CustomReadOnlyRouter()
router_readonly.register('users', UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include(router_readonly.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
