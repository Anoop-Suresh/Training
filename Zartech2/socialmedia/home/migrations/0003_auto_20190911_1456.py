# Generated by Django 2.2.5 on 2019-09-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_like_newsfeeditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeeditem',
            name='status_text',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
