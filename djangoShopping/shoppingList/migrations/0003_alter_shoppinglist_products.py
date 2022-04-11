# Generated by Django 4.0.3 on 2022-04-06 10:08

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('shoppingList', '0002_shoppinglist_edit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='products',
            field=taggit.managers.TaggableManager(help_text='Type your comma-separated list of products', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
