# Generated by Django 3.1.7 on 2021-03-15 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0018_auto_20210315_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
    ]