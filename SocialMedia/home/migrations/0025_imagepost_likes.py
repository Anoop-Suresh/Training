# Generated by Django 2.2.4 on 2019-08-13 09:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0024_imagepost_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
