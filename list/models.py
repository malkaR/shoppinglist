from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.text import slugify

class ListItem(models.Model):
    list = models.ForeignKey('List')
    item = models.CharField(max_length=50)
    quantity = models.IntegerField(null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{}- {} needed'.format(self.item, self.quantity)

    def get_absolute_url(self):
        return '/items/{}'.format(self.id)


class List(models.Model):
    user = models.ForeignKey('User')
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def list_item_count(self):
        return self.listitem_set.count()

    def add_item(self, data):
        item = ListItem(**data)
        item.list = self
        return item.save()

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        return models.Model.save(self, *args, **kwargs)

class UserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, password, is_admin=False):

        if not username:
            raise ValueError('User must have a username')
        if not first_name:
            raise ValueError('User must have a first name')
        if not last_name:
            raise ValueError('User must have a last name')

        if not is_admin and self.model.objects.filter(is_admin=False).count():
            # only one instance of a non-admin user can exist
            # update the existing values instead of creating
            existing_user = self.model.objects.get(is_admin=False)
            existing_user.username=username
            existing_user.first_name=first_name
            existing_user.last_name=last_name
            existing_user.set_password(password)
            existing_user.save()
            return existing_user
        else:
            user = self.model(
                username=username,
                first_name=first_name,
                last_name=last_name,
                is_admin=False
            )

            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, username, first_name, last_name, password):
        user = self.create_user(username,
                first_name,
                last_name,
                password,
                is_admin=True
        )

        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    is_admin = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    objects = UserManager()

    def total_item_count(self):
        return sum([list.list_item_count() for list in self.list_set.all()])

    def get_full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True




