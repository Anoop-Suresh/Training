# Generated by Django 2.2.4 on 2019-08-10 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_imagepost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
