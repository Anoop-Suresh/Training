# Generated by Django 2.2.2 on 2019-06-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_accessrecord_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessrecord',
            name='url',
        ),
        migrations.AddField(
            model_name='webpage',
            name='url',
            field=models.URLField(default='Something', unique=True),
        ),
    ]