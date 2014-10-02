from django.db import models
from django.contrib.auth.models import User

class ListItem(models.Model):
    list = models.ForeignKey('List')
    item = models.CharField(max_length=50)
    quantity = models.IntegerField(null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)



class List(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=20, default='Shopping List')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    @property
    def list_item_count(self):
        return self.listitem_set.count()

