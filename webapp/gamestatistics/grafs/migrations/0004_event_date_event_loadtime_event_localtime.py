# Generated by Django 4.1.2 on 2022-11-10 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("grafs", "0003_remove_event_date_remove_event_loadtime_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="loadTime",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="localTime",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
