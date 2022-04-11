# Generated by Django 4.0.3 on 2022-04-05 07:45

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_esuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esuser',
            name='profile_pic',
            field=models.ImageField(upload_to=accounts.models.ESUser.user_directory_path),
        ),
    ]
