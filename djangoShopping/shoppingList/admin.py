from django.contrib import admin
from .models import ShoppingList, TaggedShoppingList
# Register your models here.

admin.site.register(ShoppingList)
admin.site.register(TaggedShoppingList)
