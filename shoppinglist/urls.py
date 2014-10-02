from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from views import UserViewSet, ListItemViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'items', ListItemViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shoppinglist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
