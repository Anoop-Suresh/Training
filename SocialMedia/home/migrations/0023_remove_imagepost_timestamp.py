# Generated by Django 2.2.4 on 2019-08-13 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20190813_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='timestamp',
        ),
    ]