# Generated by Django 2.1.4 on 2018-12-17 21:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_events_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='date1',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
