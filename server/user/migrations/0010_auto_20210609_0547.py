# Generated by Django 3.2.4 on 2021-06-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_profile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_modification',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='public_key',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
