# Generated by Django 4.1.2 on 2022-11-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("grafs", "0007_alter_event_devicetype_alter_event_eventname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="sub_id",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="subuser",
            name="platformUserId",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="subuser",
            name="sub_id",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="version",
            name="sub_id",
            field=models.IntegerField(),
        ),
    ]
