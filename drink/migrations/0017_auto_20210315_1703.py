# Generated by Django 3.1.7 on 2021-03-15 14:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0016_auto_20210315_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_ordered',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 3, 15, 14, 3, 27, 282563, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
