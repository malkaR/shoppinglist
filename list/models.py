from django.db import models

class ListItem(models.Model):
    item = models.CharField(max_length=50)
    quantity = models.IntegerField(null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
