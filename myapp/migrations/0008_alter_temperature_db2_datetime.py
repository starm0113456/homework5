# Generated by Django 4.1.6 on 2023-04-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_temperature_db1_temperature_db'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature_db2',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
