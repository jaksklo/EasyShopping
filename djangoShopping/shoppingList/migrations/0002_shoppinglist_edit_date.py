# Generated by Django 4.0.3 on 2022-04-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]