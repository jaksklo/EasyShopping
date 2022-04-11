from django.db import models
from django.contrib import auth
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.utils.timezone import now

User = get_user_model()
# Create your models here.


class TaggedShoppingList(TaggedItemBase):
    content_object = models.ForeignKey('ShoppingList', on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)


class ShoppingList(models.Model):

    author = models.ForeignKey(User, related_name='shoplists', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    # products = TaggableManager(help_text="Type your comma-separated list of products", verbose_name="Products")
    products = TaggableManager(through=TaggedShoppingList, help_text="Type your comma-separated list of products", verbose_name="Products")
    created_date = models.DateTimeField(default=now, editable=False)
    edit_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('shoplists:listsbyuser', kwargs={'username': self.author.username})

    def products_as_list(self):
        listobject = []
        for item in self.products.all():
            listobject.append(item.name)

        return listobject
