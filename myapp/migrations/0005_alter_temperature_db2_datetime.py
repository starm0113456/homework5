# Generated by Django 4.1.6 on 2023-04-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_temperature_db2_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature_db2',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='創建時間'),
        ),
    ]
